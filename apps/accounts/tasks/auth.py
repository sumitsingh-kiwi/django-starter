"""
    Asynchronous task of auth
"""
# python import imports
import logging

# Third party import
from celery import shared_task
from django.contrib.auth import get_user_model

USER = get_user_model()
LOGGER = logging.getLogger('LOGGER')


@shared_task()
def logout(user_id, access_token, registration_id):
    """
    remove access_token and registration_token
    """
    try:
        LOGGER.info("going to logout user with id-{id}".format(id=user_id))
        user = USER.objects.get(pk=user_id)
        user.oauth2_provider_accesstoken.filter(token=access_token).delete()
        # remove user's push tokens
        user.fcmdevice_set.filter(registration_id=registration_id).update(active=False)
        LOGGER.info("user logged-out successfully")
    except Exception as e:
        LOGGER.error(e)
