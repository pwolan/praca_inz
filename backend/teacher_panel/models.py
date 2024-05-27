from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Classroom(models.Model):
    name = models.CharField(unique=True, max_length=100)

class UserClassrooms(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)

class Children(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'surname'], name='unique_name_surname')
        ]