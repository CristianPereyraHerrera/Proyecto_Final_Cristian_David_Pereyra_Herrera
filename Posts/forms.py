from django import forms
from Posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "subtitle", "description", "image_post"]
