from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):

    username = forms.CharField(help_text='')
    password1 = forms.CharField(help_text='', widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(help_text='', widget=forms.PasswordInput, label='Password confirmation')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')