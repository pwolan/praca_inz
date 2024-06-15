from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = RegisterForm
#     # form = CustomUserChangeForm
#     model = User
#     ordering = ("email",)
#     list_display = ["email", "first_name",]

admin.site.register(CustomUser, UserAdmin) #TODO add required email field when creating user in admin panel and remove username