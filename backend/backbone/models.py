from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from . import managers
#from backbone.models import User
from django.contrib.auth.models import User
from teacher_panel.models import Children

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consent = models.ForeignKey(Consents, on_delete=models.CASCADE)
    signing_date = models.DateTimeField(auto_now_add=True)
    seen_changes = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'consent'], name='unique_user_consent')
        ]

class History(models.Model):
    child = models.ForeignKey(Children, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='receiver')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    decision = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     #avatar = models.ImageField(null=True, blank=True)

#     objects = managers.UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'

#     def get_full_name(self):
#         '''
#         Returns the first_name plus the last_name, with a space in between.
#         '''
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         '''
#         Returns the short name for the user.
#         '''
#         return self.first_name

#     def email_user(self, subject, message, from_email=None, **kwargs):
#         '''
#         Sends an email to this User.
#         '''
#         send_mail(subject, message, from_email, [self.email], **kwargs)

#     @property
#     def is_authenticated(self):
#         return True