from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from . import manager

#from backbone.models import User


class LogType(models.TextChoices):
    LOGIN = 'LOGIN', 'Login'
    CREATE = 'CREATE', 'Create'
    DELETE = 'DELETE', 'Delete'
    IMPORT = 'IMPORT', 'Import' # import 
    ADD_PARENT = 'ADD_PARENT', 'Add Parent' # Add parent to child
    HISTORY = 'HISTORY', 'History' # Who accessed history
    ADD_PERMISSION = 'ADD_PERMISSION', 'Add Permission' # Add temporary permission
    SIGN = 'SIGN', 'Sign' # Sign consent
    WARNING = 'WARNING', 'Warning'
    ERROR = 'ERROR', 'Error'
    INFO = 'INFO', 'Info'

class ConsentType(models.TextChoices):
    INFORMATION = 'INFORMATION', 'Information'
    BIOMETRIC = 'BIOMETRIC', 'Biometric'
    # etc.

class AccessType(models.IntegerChoices):
    NONE = 0, 'None'
    PARTIAL = 1 , 'Partial'
    FULL = 2 , 'Full'

# class CustomUser(AbstractUser):
#     teacher_perm = models.PositiveSmallIntegerField(choices=AccessType.choices, default=AccessType.NONE)
#     parent_perm = models.PositiveSmallIntegerField(choices=AccessType.choices, default=AccessType.NONE)
#     email = models.EmailField(unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = manager.UserManager()

class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    teacher_perm = models.PositiveSmallIntegerField(choices=AccessType.choices, default=AccessType.NONE)
    parent_perm = models.PositiveSmallIntegerField(choices=AccessType.choices, default=AccessType.NONE)

    objects = manager.UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] #TODO what fields are required in creation

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self): #TODO change for our use
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self): #TODO change for our use
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs): #TODO create mail and connect it to project
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Logs(models.Model):
    log_type = models.CharField(max_length=20, choices=LogType.choices, default=LogType.LOGIN)
    date = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

class Consents(models.Model):
    consent_type = models.CharField(max_length=20, choices=ConsentType.choices, default=ConsentType.INFORMATION)
    change_date = models.DateTimeField(auto_now=True)
    description = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['consent_type', 'description'], name='unique_consent_type_description'),
        ]

class UserConsents(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    consent = models.ForeignKey(Consents, on_delete=models.CASCADE)
    signing_date = models.DateTimeField(auto_now_add=True)
    seen_changes = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'consent'], name='unique_user_consent')
        ]