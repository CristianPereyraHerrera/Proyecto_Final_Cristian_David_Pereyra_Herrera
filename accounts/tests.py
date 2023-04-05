from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from .models import Avatar

# Create your tests here.


class AvatarModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='usuario01', password='password01')
        self.avatar = Avatar.objects.create(user=self.user)
        self.file = SimpleUploadedFile("image.jpg", b"file_content", content_type="image/jpeg")

    @override_settings(MEDIA_ROOT='media/')
    def test_avatar_image_upload_and_delete(self):
        self.avatar.image = self.file
        self.avatar.save()
        self.assertEqual(self.avatar.image.name, 'avatars/image.jpg')

        self.avatar.image.delete()
        self.assertFalse(self.avatar.image)
