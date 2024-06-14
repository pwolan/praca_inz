from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from . import managers

class LogType(models.TextChoices):
    ERROR = 'ERROR', 'Error'
    NORMAL = 'NORMAL', 'Normal'

class Logs(models.Model):
    log_type = models.CharField(max_length=6, choices=LogType.choices, default=LogType.NORMAL)
    date = models.DateTimeField()
    data = models.JSONField()

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