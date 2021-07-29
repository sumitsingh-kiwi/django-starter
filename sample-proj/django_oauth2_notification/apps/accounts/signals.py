"""
Organization signals
"""

# django import
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

USER = get_user_model()


@receiver(post_save, sender=USER)
def update_job_detail(sender, instance, created, **kwargs):
    """
    this method is called on USER model post_save signal
    """
    if created:
        # create application if a new user is being created
        instance.create_application()
