from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, UserChangeForm
from django.contrib.auth.views import PasswordResetConfirmView
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model = User
        fields = ['email']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar', 'phone_number', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
