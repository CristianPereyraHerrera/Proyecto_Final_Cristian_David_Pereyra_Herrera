from django import forms
from django.contrib.auth.models import User
from accounts.models import Avatar


class UserRegisterForm(forms.ModelForm):
    image = forms.ImageField()
    description = forms.CharField(max_length=200, required=False)
    website = forms.URLField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', 'description', 'website')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
