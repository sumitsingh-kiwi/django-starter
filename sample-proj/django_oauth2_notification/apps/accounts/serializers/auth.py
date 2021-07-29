"""
auth serializer file
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.accounts.messages import ERROR_CODE, SUCCESS_CODE

USER = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    """ used to verify the login credentials and return the login response """
    email = serializers.EmailField(max_length=100)

    class Meta:
        """ meta class """
        model = USER
        fields = ('email', 'password')

    def validate(self, attrs):
        """ used to validate the email and password """
        user = USER.objects.filter(email__iexact=attrs['email']).first()
        if not user:
            raise serializers.ValidationError({'detail': ERROR_CODE['4001']})
        if not user.is_active:
            raise serializers.ValidationError({'detail': ERROR_CODE['4003']})
        if not user.is_verified:
            raise serializers.ValidationError({'detail': ERROR_CODE['4005']})
        if not user.check_password(attrs['password']):
            raise serializers.ValidationError({'detail': ERROR_CODE['4002']})
        self.context.update({'user': user})
        return attrs

    def create(self, validated_data):
        """ used to return the user object """
        return self.context['user']

    def to_representation(self, instance):
        """ used to return the user json """
        return {'token': instance.get_token()}


class RegisterSerializer(serializers.ModelSerializer):
    """ used to register the user """

    class Meta:
        """ meta class """
        model = USER
        fields = ('first_name', 'email', 'password')

    def validate(self, attrs):
        """ used to validate the data"""
        user = USER.objects.filter(email__iexact=attrs['email']).first()
        if user:
            raise serializers.ValidationError({'detail': ERROR_CODE['4004']})
        return attrs

    def create(self, validated_data):
        """ used to return the user object """
        user = USER.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, instance):
        """ used to return the user json """
        return {'detail': SUCCESS_CODE['2001']}


class LogoutSerializer(serializers.Serializer):
    """
    used to logout the user
    """
    registration_id = serializers.CharField(max_length=250, required=False)

    class Meta:
        """
        meta class
        """
        fields = ('registration_id', )


class UserDetailSerializer(serializers.ModelSerializer):
    """ used to serialize the user model """

    class Meta:
        model = USER
        fields = ('id', 'first_name', 'last_name', 'profile_picture')
