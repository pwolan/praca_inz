from django.contrib.auth.base_user import BaseUserManager

from . import types

class UserManager(BaseUserManager):

    use_in_migrations = True
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email), first_name=first_name, last_name=last_name, **extra_fields
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('teacher_perm', types.AccessType.FULL)
        extra_fields.setdefault('parent_perm', types.AccessType.FULL)

        return self.create_user(email, first_name, last_name, password, **extra_fields)

# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, email, first_name, last_name, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
#         print(email, first_name, last_name, password)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_user(self, email, first_name, last_name, password=None, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, first_name, last_name, password, **extra_fields)

#     def create_superuser(self, email, first_name, last_name, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, first_name, last_name, password, **extra_fields)