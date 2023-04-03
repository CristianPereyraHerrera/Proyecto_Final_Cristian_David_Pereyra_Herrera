from django.contrib.auth.models import User
from django.db import models


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatars", null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.image.name
