"""
urls file
"""
# third party imports
from django.conf.urls import url

# local imports
from apps.web_admin.views.auth import ForgotPasswordView, LoginView, DashboardView, Logout

urlpatterns = [
    url('forgot-password', ForgotPasswordView.as_view(), name='forgot-password'),
    url('logout', Logout.as_view(), name='logout'),
    url('dashboard', DashboardView.as_view(), name='dashboard'),
    url('', LoginView.as_view(), name='login'),
]
