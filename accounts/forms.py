from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ["username", "email", "password"]
