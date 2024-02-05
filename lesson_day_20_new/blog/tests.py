from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "testuser", email = "test@gmail.com", password = "secret"
        )
        cls.post = Post.object.create(
            title = "A good title",
            body = "Nice body content",
            author = cls.user,
           )
    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(str(self.post), "a good title")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")