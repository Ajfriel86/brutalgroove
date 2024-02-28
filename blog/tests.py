from blog.models import Post
from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from os import path
from blog.forms import ContactForm
from .views import CombinedHomeView
from .admin import CommentAdmin
from .models import Comment
from unittest.mock import patch
from django.contrib.admin.sites import AdminSite

# Models Testing


class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Setup non-modified objects used by all test methods
        cls.user = User.objects.create(username='testuser')
        cls.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=cls.user,
            content='Test Content',
            status=1
        )

    def test_number_of_likes(self):
        # Test the custom method number_of_likes
        self.assertEqual(self.post.number_of_likes(), 0)

# Forms Testing


class ContactFormTest(TestCase):

    def test_contact_form_valid(self):
        form_data = {'name': 'John Doe', 'email': 'john@example.com',
                     'subject': 'Test Subject', 'message': 'Test message'}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid(self):
        form_data = {}  # Empty data
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        # Expecting errors for all fields
        self.assertEqual(len(form.errors), 4)


#  Views Testingfrom django.test import TestCase

class CombinedHomeViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user for author
        cls.user = User.objects.create_user(
            username='testuser', password='password123')
        # Create test posts with author
        for post_num in range(10):
            Post.objects.create(
                title=f'Post {post_num}',
                content='Content...',
                status=1,  # Published
                author=cls.user,
            )

# URLS testing


class UrlsTest(TestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, CombinedHomeView)

# Admin Testingfrom django.contrib.admin.sites import AdminSite


class MockRequest:
    pass


request = MockRequest()


class CommentAdminTest(TestCase):

    def test_approve_comments_action(self):
        # Assuming comments exist in the test DB
        site = AdminSite()
        admin = CommentAdmin(Comment, site)
        queryset = Comment.objects.filter(approved=False)
        admin.approve_comments(request, queryset)
        for comment in queryset:
            self.assertTrue(comment.approved)

# mock tests


class PostLikeTest(TestCase):
    def setUp(self):
        # Create a user for the test case
        self.user = User.objects.create_user(
            'testuser', 'test@example.com', 'password')

        # Create a post and assign the created user as the author
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content.',
            author=self.user  # Assign the user as the author
        )


class ContactViewTest(TestCase):
    def test_contact_form_submission(self):
        form_data = {
            'name': 'Test Name',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message',
        }
        response = self.client.post(reverse('contact'), data=form_data)
        # Adjusted to check redirection to the 'registration_success' URL
        self.assertRedirects(response, reverse(
            'registration_success'), status_code=302, target_status_code=200)
