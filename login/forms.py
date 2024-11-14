from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Foydalanuvchi nomi', max_length=50)
    password = forms.CharField(label='Parol', widget=forms.PasswordInput)