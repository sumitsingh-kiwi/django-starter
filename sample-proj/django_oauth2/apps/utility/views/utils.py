"""
utility views
"""
from django.contrib.auth.decorators import login_required
from django.core.management import call_command
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View

from apps.utility.constants import FIXTURES
from apps.utility.messages import SUCCESS_CODE


class LoadFixtures(View):
    """
    Set the primary-email of the recruiter to the updated one
    """
    @method_decorator(login_required)
    def get(self, request):
        fixture_type = request.GET.get('fixture_type')
        if fixture_type:
            try:
                call_command('loaddata', FIXTURES[fixture_type])
            except (KeyError, TypeError) as e:
                return HttpResponse(str(e))
        return HttpResponse(SUCCESS_CODE['2000'])
