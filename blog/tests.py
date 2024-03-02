from django.test import TestCase  # Import TestCase for creating test cases.
# Import reverse to reverse resolve URLs,
# resolve to match requested URLs to their view functions.
from django.urls import reverse, resolve
# Import the User model to test user-related functionality.
from django.contrib.auth.models import User
# Import Post and Comment models for testing.
from blog.models import Post, Comment
# Import the ContactForm for form validation testing.
from blog.forms import ContactForm
# Import CombinedHomeView for view testing.
from blog.views import CombinedHomeView
# Import CommentAdmin for admin interface testing.
from blog.admin import CommentAdmin
# Import AdminSite to create an instance of the Django admin site for testing.
from django.contrib.admin.sites import AdminSite
# Import patch for mocking objects during testing.
from unittest.mock import patch


# Models Testing


class PostModelTests(TestCase):
    """TestCase class to test the functionality of the Post model."""

    @classmethod
    def setUpTestData(cls):
        """Setup non-modified objects used by all test methods."""
        cls.user = User.objects.create(username='testuser')
        cls.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=cls.user,
            content='Test Content',
            status=1
        )

    def test_number_of_likes(self):
        """Test the custom method number_of_likes."""
        self.assertEqual(self.post.number_of_likes(), 0)

# Forms Testing


class ContactFormTest(TestCase):
    """TestCase class to test the validity of the ContactForm."""

    def test_contact_form_valid(self):
        """Test the ContactForm with valid data."""
        form_data = {'name': 'John Doe', 'email': 'john@example.com',
                     'subject': 'Test Subject', 'message': 'Test message'}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_invalid(self):
        """Test the ContactForm with invalid (empty) data."""
        form_data = {}  # Empty data
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        # Expecting errors for all fields
        self.assertEqual(len(form.errors), 4)

# Views Testing


class CombinedHomeViewTests(TestCase):
    """TestCase class to test the CombinedHomeView view."""

    @classmethod
    def setUpTestData(cls):
        """Create a user and multiple posts for testing the home view."""
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
    """TestCase class to test URL resolution."""

    def test_home_url_resolves(self):
        """Ensure the home URL resolves to the correct view."""
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, CombinedHomeView)

# Admin Testing


class MockRequest:
    """A mock request class for simulating HTTP requests in admin tests."""


request = MockRequest()


class CommentAdminTest(TestCase):
    """TestCase class to test admin actions for the Comment model."""

    def test_approve_comments_action(self):
        """Test the 'approve_comments' action in the CommentAdmin."""
        site = AdminSite()
        admin = CommentAdmin(Comment, site)
        queryset = Comment.objects.filter(approved=False)
        admin.approve_comments(request, queryset)
        for comment in queryset:
            self.assertTrue(comment.approved)

# Mock tests


class PostLikeTest(TestCase):
    """A TestCase for testing 'like' functionality on Post model."""

    def setUp(self):
        """Create a user and a post for the like functionality test."""
        self.user = User.objects.create_user(
            'testuser', 'test@example.com', 'password')
        self.post = Post.objects.create(
            title='Test Post', content='Test content.', author=self.user)


class ContactViewTest(TestCase):
    """TestCase class to test the contact form submission view."""

    def test_contact_form_submission(self):
        """Test the submission of the contact form
        and redirect to success page."""
        form_data = {
            'name': 'Test Name',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message',
        }
        response = self.client.post(reverse('contact'), data=form_data)
        # Check redirection to the 'registration_success' URL
        self.assertRedirects(response, reverse(
            'registration_success'), status_code=302, target_status_code=200)
