"""
auth views
"""
# django imports
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from rest_framework import status
from rest_framework.viewsets import GenericViewSet, mixins

# local imports
from apps.accounts.forms.reset_password import ResetPasswordForm
from apps.accounts.messages import SUCCESS_CODE, ERROR_CODE
from apps.accounts.serializers.auth import (LoginSerializer, RegisterSerializer, UserDetailSerializer, LogoutSerializer,
                                            ForgotPasswordSerializer)
from apps.accounts.tasks.auth import logout

USER = get_user_model()


# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class LoginViewSet(GenericViewSet, mixins.CreateModelMixin):
    """
    used to login the user and return the token info
        POST  /login/
        request body: {"email": "example@email.com", "password": "my-password"}
        content-type: Application/json
    """
    serializer_class = LoginSerializer


class RegisterViewSet(GenericViewSet, mixins.CreateModelMixin):
    """
    used to register the user and return the token info
    POST  /signup/
        request body: {
                          "first_name": "string",
                          "email": "user@example.com",
                          "password": "string"
                        }
        content-type: Application/json
    """
    serializer_class = RegisterSerializer


class LogoutViewSet(GenericViewSet, mixins.CreateModelMixin):
    """
     Logout view is used for user logout.
     """
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def create(self, request, *args, **kwargs):
        """
        :param request: request user
        :param args: argument list
        :param kwargs: keyword argument object
        :return: logout a user
        """
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        logout.delay(request.user.id, request.META['HTTP_AUTHORIZATION'].split(" ")[1])
        return Response({'message': SUCCESS_CODE["2000"], 'data': None},
                        status=status.HTTP_200_OK)


class ProfileViewSet(GenericViewSet, mixins.RetrieveModelMixin):
    """
    used to get the user details
    POST  /profile/{user-id}
    content-type: Application/json
    """
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = USER.objects.filter(is_active=True)


class ForgotPasswordViewSet(GenericViewSet, mixins.CreateModelMixin):
    """
    forgot password
    """
    serializer_class = ForgotPasswordSerializer

    def create(self, request):
        forgot_password_serializer = self.serializer_class(data=request.data)
        forgot_password_serializer.is_valid(raise_exception=True)
        forgot_password_serializer.save()
        return Response({'detail': SUCCESS_CODE["2000"], 'data': None},
                        status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(View):
    """ used to reset the user's forgot password """
    form_class = ResetPasswordForm
    
    def get(self, request):
        """ used to render the reset-password html """
        return render(request, 'auth/reset-password.html')

    def post(self, request):
        """ used to reset the user password """
        form = ResetPasswordForm(data=request.POST)
        if form.is_valid():
            if request.POST['new_password'] != request.POST['confirm_password']:
                messages.error(request, ERROR_CODE['4006'])
                return redirect(reverse('account:v1:reset-password') + "?token={}&email={}".format(
                    request.POST.get('token', ''), request.POST.get('email', '')))
            user = USER.objects.filter(email__iexact=request.POST['email'].lower(),
                                       forgot_pass_token=request.POST['token']).first()
            if not user:
                messages.error(request, ERROR_CODE['4007'])
                return redirect(reverse('account:v1:reset-password') + "?token={}&email={}".format(
                    request.POST.get('token', ''), request.POST.get('email', '')))

            user.set_password(request.POST['new_password'])
            user.forgot_pass_token = ""
            user.forgot_pass_token_created_at = None
            user.save()
            messages.success(request, SUCCESS_CODE['2003'])
            return render(request, 'auth/reset-success.html', {'front_end_url': settings.FRONT_END_URL})
        messages.error(request, ERROR_CODE['4007'])
        return redirect(reverse('account:v1:reset-password') + "?token={}&email={}".format(
            request.POST.get('token', ''), request.POST.get('email', '')))
