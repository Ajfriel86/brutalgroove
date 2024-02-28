from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from .forms import ContactForm
from django.urls import reverse
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
        # Create a user and a post
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.post = Post.objects.create(
            title='Test Post', content='Test Content', status=1)

    def test_like_post_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(
            reverse('post_like', args=[self.post.slug]), {}, HTTP_REFERER='/')
        self.post.refresh_from_db()
        self.assertEqual(self.post.likes.count(), 1)


class ContactViewTest(TestCase):

    @patch('path.to.your.ContactForm.save')
    def test_contact_form_submission(self, mock_save):
        response = self.client.post(reverse('contact'), data={
                                    'name': 'Test', 'email': 'test@example.com', 'message': 'Hello'})
        # Assuming redirection to a success page
        self.assertEqual(response.status_code, 302)
        self.assertTrue(mock_save.called)
