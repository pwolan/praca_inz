from django.contrib import admin

from .models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class MyUserAdmin(UserAdmin):
    form = CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informacje", {"fields": ("first_name", "last_name", "phone_number", "last_login", "date_joined")}),
        ("Pozwolenia", {"fields": ("teacher_perm", "parent_perm", "is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    

admin.site.register(CustomUser, CustomUserAdmin) #TODO add required email field when creating user in admin panel and remove username
admin.site.register(Log) 
admin.site.register(Consent) 
admin.site.register(UserConsent) 