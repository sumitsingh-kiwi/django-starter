"""
urls file
"""
# third party imports
from django.conf.urls import url
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

# local imports
from apps.accounts.views.auth import (LoginViewSet, RegisterViewSet, ProfileViewSet, ForgotPasswordViewSet,
                                      ResetPasswordView)

router = routers.SimpleRouter()

router.register('login', LoginViewSet, basename='login')
router.register('signup', RegisterViewSet, basename='signup')
router.register('profile', ProfileViewSet, basename='profile')
router.register('forgot-password', ForgotPasswordViewSet, basename='forgot-password')

urlpatterns = [
    url('reset-password', ResetPasswordView.as_view(), name='reset-password'),
    url('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
