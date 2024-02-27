from django.db import models  # Import models module from django.db
# Import User model from django.contrib.auth.models
from django.contrib.auth.models import User
# Import CloudinaryField from cloudinary.models
from cloudinary.models import CloudinaryField

# Define choices for post status
STATUS = ((0, "Draft"), (1, "Published"))

# Define Post model for blog posts


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Title of the post
    # Slug for SEO-friendly URL
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")  # Author of the post
    # Featured image for the post using Cloudinary
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)  # Excerpt of the post
    # Date and time when the post was last updated
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()  # Content of the post
    # Date and time when the post was created
    created_on = models.DateTimeField(auto_now_add=True)
    # Status of the post (Draft or Published)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)  # Users who liked the post

    class Meta:
        # Order posts by created_on date in descending order
        ordering = ["-created_on"]

    def __str__(self):
        return self.title  # String representation of the post

    def number_of_likes(self):
        return self.likes.count()  # Number of likes for the post

# Define Comment model for comments on blog posts


class Comment(models.Model):
    # Post the comment belongs to
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="user_comments")  # Author of the comment
    name = models.CharField(max_length=80)  # Name of the commenter
    email = models.EmailField()  # Email of the commenter
    body = models.TextField()  # Content of the comment
    # Date and time when the comment was created
    created_on = models.DateTimeField(auto_now_add=True)
    # Approval status of the comment
    approved = models.BooleanField(default=False)

    class Meta:
        # Order comments by created_on date in ascending order
        ordering = ["created_on"]

    def __str__(self):
        # String representation of the comment
        return f"Comment {self.body} by {self.name}"

# Define Contact model for storing contact form submissions


class Contact(models.Model):
    # Name of the person submitting the form
    name = models.CharField(max_length=100)
    email = models.EmailField()  # Email of the person submitting the form
    subject = models.CharField(max_length=255)  # Subject of the message
    message = models.TextField()  # Content of the message
    # Date and time when the submission was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # String representation of the contact form submission
        return f"{self.name} - {self.subject}"

# Define HeroImage model for hero images


class HeroImage(models.Model):
    title = models.CharField(max_length=200)  # Title of the hero image
    # Caption for the hero image
    caption = models.TextField(blank=True, null=True)
    image = CloudinaryField('image')  # Hero image using Cloudinary
    # Activation status of the hero image
    is_active = models.BooleanField(default=False)
    # Date and time when the hero image was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # String representation of the hero image

    class Meta:
        # Order hero images by created_at date in descending order
        ordering = ['-created_at']
