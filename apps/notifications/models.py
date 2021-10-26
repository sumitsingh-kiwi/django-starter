"""
models file
"""
# django imports
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

USER = get_user_model()
# Create your models here.


class NotificationType(models.Model):
    """ record all notificaiton types """
    name = models.CharField(max_length=50)
    data = models.JSONField(default=dict)
    save_to_db = models.BooleanField(default=True)
    send_push = models.BooleanField(default=True)
    send_sms = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """ string representation """
        return self.name


class Notification(models.Model):
    """ used to save the notifications """
    notification_type = models.ForeignKey(NotificationType, related_name='related_notifications',
                                          on_delete=models.CASCADE)
    notification_to = models.ForeignKey(USER, related_name='my_notification', on_delete=models.CASCADE)
    notification_from = models.ForeignKey(USER, related_name='from_notification', on_delete=models.SET_NULL,
                                          blank=True, null=True)
    data = models.JSONField(default=dict)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """ string representation """
        return self.notification_to.first_name
