from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='usuario01', password='password01')

    def test_create_and_delete_post(self):
        post = Post.objects.create(
            user=self.user,
            title='Test post',
            subtitle='Test subtitle',
            description='Test description',
        )
        self.assertEqual(Post.objects.count(), 1)
        post.delete()
        self.assertEqual(Post.objects.count(), 0)
