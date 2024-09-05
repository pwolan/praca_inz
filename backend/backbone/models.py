from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from . import manager, types

# models: CustomUser, Log, Consent, UserConsent

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=16, default="", blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    teacher_perm = models.PositiveSmallIntegerField(choices=types.AccessType.choices, default=types.AccessType.NONE)
    parent_perm = models.PositiveSmallIntegerField(choices=types.AccessType.choices, default=types.AccessType.NONE)

    objects = manager.UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs): #TODO create mail and connect it to project
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = "User" # "Użytkownik"
        verbose_name_plural = "Users" # "Użytkownicy"

class Log(models.Model):
    log_type = models.CharField(max_length=16, choices=types.LogType.choices, default=types.LogType.LOGIN)
    date = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    class Meta:
        verbose_name = "Log" # "Log"
        verbose_name_plural = "Logs" # "Logi"

class Consent(models.Model):
    consent_type = models.CharField(max_length=16, choices=types.ConsentType.choices, default=types.ConsentType.INFORMATION)
    change_date = models.DateTimeField(auto_now=True)
    description = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['consent_type', 'description'], name='unique_consent_type_description'),
        ]
        verbose_name = "Consent" # "Zgoda"
        verbose_name_plural = "Consents" # "Zgody"

class UserConsent(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    consent = models.ForeignKey(Consent, on_delete=models.CASCADE)
    signing_date = models.DateTimeField(auto_now_add=True)
    seen_changes = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'consent'], name='unique_user_consent')
        ]
        verbose_name = "User-Consent" # "Zgoda Użytkownika"
        verbose_name_plural = "Users-Consents" # "Zgody Użytkownika"
