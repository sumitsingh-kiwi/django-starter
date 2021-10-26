"""
push notification utils
"""
# django imports
from celery import shared_task
from django.contrib.auth import get_user_model
from fcm_django.models import FCMDevice

# local imports
from apps.notifications.models import NotificationType, Notification

USER = get_user_model()


def register_fcm_token(user, registration_id, device_type):
    """ used to register the fcm device token"""
    device, _ = FCMDevice.objects.get_or_create(registration_id=registration_id)
    device.user = user
    device.type = device_type
    device.active = True
    device.save()
    return device


def get_basic_detail(notification_type, from_user_id, to_user_id):
    """ used to get the basic details """
    notification_obj = NotificationType.objects.get(name=notification_type)
    from_user = USER.objects.get(id=from_user_id) if from_user_id else None
    to_user = USER.objects.get(id=to_user_id)
    return notification_obj, from_user, to_user


def send_push(user, data):
    """ used to send push notification to specific user """
    if user.push_notification:
        user.fcmdevice_set.filter(active=True).send_message(**data)


@shared_task()
def send_notification(notification_type, from_user_id, to_user_id, extra_data):
    """ used to send the push for the given notification type """
    (notification_type_obj, from_user, to_user) = get_basic_detail(notification_type, from_user_id, to_user_id)
    data = notification_type_obj.data
    data['body'] = data['body'].format(**extra_data)
    if notification_type_obj.save_to_db:
        Notification.objects.create(notification_type=notification_type_obj, notification_from=from_user,
                                    notification_to=to_user, data=data)
    if notification_type_obj.send_push:
        data.update({'badge': Notification.objects.filter(notification_to=to_user, is_read=False).count()})
        to_user.send_push(data)
