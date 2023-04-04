from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    user_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sent')
    user_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_received')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.user_sender} to {self.user_receiver}'
