"""
models file
"""
# django imports
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from oauth2_provider.models import Application, AccessToken
from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token

# local imports
from apps.accounts.choices import GENDER
from apps.accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    User Model Class
    """
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    country_code = models.CharField(max_length=5, null=True, blank=True)
    contact_number = models.CharField(max_length=17, null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=2, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='user')
    dob = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=20, blank=True, null=True)
    verification_token_created_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)

    # here username_field is django defined field in account model, used for account identification.
    USERNAME_FIELD = 'email'

    # list of the field names that will be prompted for when creating a account via the
    # createsuperuser management command.
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.id and not self.user_name:
            self.user_name = self.email
            
        super(User, self).save(*args, **kwargs)

    def create_application(self):
        """
        here we are creating application for user
        """
        Application.objects.get_or_create(user=self, client_type=Application.CLIENT_CONFIDENTIAL,
                                          authorization_grant_type=Application.GRANT_PASSWORD)

    def get_token(self):
        """
        :return: access-token in json format
        """
        app = Application.objects.get(user=self)
        token = generate_token()
        expires = timezone.now() + timezone.timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
        scope = "read write"
        AccessToken.objects.create(user=self, application=app, expires=expires, token=token, scope=scope)

        token = {
            'access_token': token,
            'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
        }
        return token
