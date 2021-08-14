"""
utility urls file
"""
# third party imports
from django.urls import path

# local imports
from apps.utility.views.utils import LoadFixtures

urlpatterns = [
    path('load_fixtures/', LoadFixtures.as_view(), name="load_fixtures"),
]
