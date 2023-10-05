from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from userapp.models import BbUser


# from django import forms


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


# class RegisterUserForm(forms.ModelForm):
class RegisterUserForm(UserCreationForm):
    # password1 = forms.CharField(label='Пароль')
    # password2 = forms.CharField(label='Пароль (повторно)')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'age')
        # fields = ('username', 'email', 'first_name', 'last_name')
