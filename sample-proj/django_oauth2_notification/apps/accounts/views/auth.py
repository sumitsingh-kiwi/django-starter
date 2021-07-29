"""
auth views
"""
# django imports
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins

# local imports
from apps.accounts.messages import SUCCESS_CODE
from apps.accounts.serializers.auth import LoginSerializer, RegisterSerializer, UserDetailSerializer, LogoutSerializer
from apps.accounts.tasks.auth import logout

USER = get_user_model()


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
        logout.delay(request.user.id, request.META['HTTP_AUTHORIZATION'].split(" ")[1],
                     request.data.get('registration_id', ""))
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
