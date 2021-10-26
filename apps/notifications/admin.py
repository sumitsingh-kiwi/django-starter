"""
admin file
"""
# django imports
from django.contrib import admin

# local imports
from apps.notifications.models import NotificationType, Notification


@admin.register(NotificationType)
class NotificationTypeAdmin(admin.ModelAdmin):
    """
    admin interface for NotificationType.
    """
    list_display = ('id', 'name', 'save_to_db', 'send_push', 'send_sms')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """
    admin interface for Notification.
    """
    list_display = ('id', 'notification_to', 'notification_from', 'notification_type', 'created_at')
