"""
urls file
"""
# third party imports
from rest_framework import routers

# local imports
from apps.accounts.views.auth import LoginViewSet, RegisterViewSet, ProfileViewSet

router = routers.SimpleRouter()

router.register('login', LoginViewSet, basename='login')
router.register('signup', RegisterViewSet, basename='signup')
router.register('profile', ProfileViewSet, basename='profile')

urlpatterns = [
] + router.urls
