from django import forms
from django.contrib.auth.models import User


class MessageForm(forms.Form):
    user_username = forms.CharField(label='Recipient username')
    content = forms.CharField(widget=forms.Textarea)

    def clean_user_username(self):
        username = self.cleaned_data['user_username']
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError('The receiving user does not exist.')
        return username
