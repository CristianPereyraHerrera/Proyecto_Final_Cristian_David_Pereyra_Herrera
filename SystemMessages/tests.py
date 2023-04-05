from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message

# Create your tests here.


class MessageModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='usuario01', email='usuario01@gmail.com', password='password01')
        self.user2 = User.objects.create_user(
            username='usuario02', email='usuario02@gmail.com', password='password02')

    def test_send_message(self):
        message = Message.objects.create(
            user_sender=self.user1,
            user_receiver=self.user2,
            content='Test message'
        )

        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(message.user_sender, self.user1)
        self.assertEqual(message.user_receiver, self.user2)
        self.assertEqual(message.content, 'Test message')
