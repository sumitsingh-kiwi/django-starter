"""
web admin auth views
"""
# django imports
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

# local imports
from apps.web_admin.forms.auth import LoginForm, ForgotPasswordForm
from apps.web_admin.messages import ERROR_CODE, SUCCESS_CODE

USER = get_user_model()


class LoginView(TemplateView):
    """ login view set """
    template_name = 'auth/login.html'

    def post(self, request):
        """ login view """
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(email=request.POST['email'].lower(),
                                password=request.POST['password'])

            if not user or not user.is_superuser:
                messages.error(request, ERROR_CODE['4001'])
                return render(
                    request=request,
                    template_name=self.template_name,
                    context={})
            login(request, user)
            return redirect(reverse("web_admin:v1:dashboard"))
        messages.error(request, ERROR_CODE['4001'])
        return render(request=request,
                      template_name=self.template_name,
                      context={})


class Logout(LoginRequiredMixin, TemplateView):
    """ logout view """
    template_name = '/auth/login.html'

    def get(self, request, **kwargs):
        """ used to logout the admin user """
        logout(request)
        return redirect(reverse('web_admin:v1:login'))


class ForgotPasswordView(TemplateView):
    """ forgot password view for admin """
    template_name = 'auth/forgot-password.html'

    def post(self, request, **kwargs):
        """
        :param request: wsgi request object
        :return:
        """
        forgot_form = ForgotPasswordForm(request.POST)
        if forgot_form.is_valid():
            user = USER.objects.filter(email__iexact=request.POST['email'].lower(), is_superuser=True).first()
            if user:
                user.send_forgot_pass_mail()
                messages.success(request, SUCCESS_CODE['2001'])
            else:
                messages.error(request, ERROR_CODE['4002'])
            return render(request=request, template_name=self.template_name, context={})
        messages.error(request, ERROR_CODE['4000'])
        return render(request=request, template_name=self.template_name, context={})


class DashboardView(TemplateView):
    """ used to show the dashboard view """
    template_name = 'dashboard/dashboard.html'
