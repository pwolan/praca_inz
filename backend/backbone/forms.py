# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from .models import User
# #from django.contrib.auth.models import User

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(label = "Email (test)")
#     password = forms.CharField(label = "Password (test)")

#     class Meta:
#         model = User
#         fields = ("email", "first_name", "last_name", "password" )

#     def save(self, commit=True):
#         user = super(RegisterForm, self).save(commit=False)
#         user.first_name = self.cleaned_data["first_name"]
#         user.last_name = self.cleaned_data["last_name"]
#         user.email = self.cleaned_data["email"]
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user