"""
notification serializers
"""
# django imports
from rest_framework import serializers

# local imports
from apps.accounts.serializers.auth import UserDetailSerializer
from apps.notifications.models import Notification, NotificationType
from apps.notifications.push_notification_utils import register_fcm_token


class NotificationTypeSerializer(serializers.ModelSerializer):
    """ used to serialize the NotificationType model """
    class Meta:
        """ meta class """
        model = NotificationType
        exclude = ('save_to_db', 'send_sms', 'send_push', 'is_active')


class NotificationListSerializer(serializers.ModelSerializer):
    """ used to serialize the Notification model """
    notification_type = NotificationTypeSerializer()
    notification_to = UserDetailSerializer()
    notification_from = UserDetailSerializer()

    class Meta:
        """ meta class """
        model = Notification
        fields = '__all__'


class RegisterDevice(serializers.Serializer):
    """
    used to create and validate register device token
    """
    registration_id = serializers.CharField(max_length=250)
    type = serializers.ChoiceField(choices=["ios", "web", "android"])

    class Meta:
        """ meta class """
        fields = ('registration_id', 'type')

    def create(self, validated_data):
        """ override this method to create device token for users """
        registration_id = validated_data['registration_id']
        device_type = validated_data['type']
        return register_fcm_token(self.context['user'], registration_id, device_type)