from django.db import models
#from backbone.models import User
from backbone.models import CustomUser as User

# Create your models here.

class Classroom(models.Model):
    name = models.CharField(unique=True, max_length=100)

class UserClassrooms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'classroom'], name='unique_user_classroom')
        ]

class Children(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    birth_date = models.DateField(max_length=8)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'surname', 'birth_date'], name='unique_name_surname_birth_date')
        ]

class UserChildren(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    child = models.ForeignKey(Children, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'child'], name='unique_user_child')
        ]

class History(models.Model):
    child = models.ForeignKey(Children, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='receiver')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    decision = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
