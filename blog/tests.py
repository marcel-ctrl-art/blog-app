from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post


class PostModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='testtile',
            text='test-text',
            author=self.user)

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword')
