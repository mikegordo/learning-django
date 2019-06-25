from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from .models import Post, Comment


# Create your tests here.

class TestThings(TestCase):

    def setUp(self):
        self.client = Client()

    def test_assertion(self):
        self.assertEquals(5, 5, 'unexpected failure')

    def tst_user(self):
        User.objects.create(username="john.smith",
                            password="^gh*Daq%^3",
                            email="john.smith@company.com")

        all = User.objects.all()
        self.assertEquals(all.count(), 1)
        self.assertEquals(all[0].email, "john.smith@company.com")

    def tst_post(self):
        user = User.objects.get(username="john.smith")

        Post.objects.create(title="Once upon a time",
                            author=user,
                            slug="once-upon-a-time",
                            body="Once upon a time in a galaxy far far away")

        all = Post.objects.all()
        self.assertEquals(all.count(), 1)
        self.assertEquals(all[0].slug, "once-upon-a-time")

    def tst_comment(self):
        post = Post.objects.get(slug="once-upon-a-time")
        Comment.objects.create(post=post,
                               name="John Smith",
                               email="john.smith@company.com",
                               body="Really great post!")

        all = Comment.objects.all()
        self.assertEquals(all.count(), 1)
        self.assertEquals(all[0].name, "John Smith")

    def test_user_post_comment(self):
        self.tst_user()
        self.tst_post()
        self.tst_comment()
