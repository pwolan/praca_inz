from datetime import timedelta

from django.db import models
from django.utils import timezone

from backbone.models import CustomUser as User
from teacher_panel.models import Children
from backbone.types import PermissionState

# models: UserChildren, History, PermittedUser, Permission

class UserChildren(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    child = models.ForeignKey(Children, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'child'], name='unique_parent_child')
        ]
        verbose_name = "User-Child" # "Dziecko Użytkownika"
        verbose_name_plural = "Users-Children" # "Dzieci Użytkownika"

class History(models.Model):
    child = models.ForeignKey(Children, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='receiver')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    decision = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "History" # "Historia"
        verbose_name_plural = "History" # "Historia"

class PermittedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    child = models.ForeignKey(Children, on_delete=models.CASCADE)
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="parent")
    date = models.DateTimeField(default=timezone.now)
    signature_delivered = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'child'], name='unique_receiver_child'),
        ]
        verbose_name = "PermittedUser" # "Dozwolony Użytkownik"
        verbose_name_plural = "PermittedUsers" # "Dozwoleni Użytkownicy"

class Permission(models.Model):
    permitteduser = models.ForeignKey(PermittedUser, on_delete=models.CASCADE)
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=6, choices=PermissionState.choices, default=PermissionState.SLEEP)
    qr_code = models.CharField(max_length=254)
    two_factor_code = models.IntegerField() #TODO validator so it accepts only 8-number integers
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = "Permission" # "Uprawnienie"
        verbose_name_plural = "Permissions" # "Uprawnienia"
