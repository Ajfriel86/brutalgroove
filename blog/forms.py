from .models import Comment  # Import Comment model
from .models import Contact  # Import Contact model
from django import forms  # Import forms module from django


class CommentForm(forms.ModelForm):
    """
    A form for creating and submitting a comment.
    This form is linked to the
    Comment model and includes only the
    'body' field for submission.
    """
    class Meta:
        # Specify the model to be used for the form
        model = Comment
        # Specify the fields to be included in the form
        fields = ('body',)


class ContactForm(forms.ModelForm):
    """
    A form for submitting contact information and messages.
    This form is linked
    to the Contact model and includes fields for name,
    email, subject, and message.
    It is used to facilitate users in sending
    messages or inquiries.
    """
    class Meta:
        # Specify the model to be used for the form
        model = Contact
        # Specify the fields to be included in the form
        fields = ['name', 'email', 'subject', 'message']
