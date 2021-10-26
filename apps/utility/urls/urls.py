"""
util's urls
"""
# third party imports
from django.urls import path, include

urlpatterns = [
    path('v1/', include(('apps.utility.urls.v1_urls', 'v1'), namespace='v1')),
]
