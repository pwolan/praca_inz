from django.contrib import admin

from .models import *

# class CustomUserAdmin(UserAdmin):
#     add_form = RegisterForm
#     # form = CustomUserChangeForm
#     model = User
#     ordering = ("email",)
#     list_display = ["email", "first_name",]

admin.site.register(CustomUser) #TODO add required email field when creating user in admin panel and remove username
admin.site.register(Log) 
admin.site.register(Consent) 
admin.site.register(UserConsent) 