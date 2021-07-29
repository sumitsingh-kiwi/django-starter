"""
    Url file of notification app.
"""
# django imports
from django.conf.urls import url, include
from rest_framework import routers

# local imports
from apps.notifications.views import NotificationViewSet

router = routers.SimpleRouter()

router.register(r'notifications', NotificationViewSet, basename='notifications')

urlpatterns = [
    url(r'', include(router.urls))
]
