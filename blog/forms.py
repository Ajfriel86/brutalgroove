from .models import Comment  # Import Comment model
from .models import Contact  # Import Contact model
from django import forms  # Import forms module from django

# Define CommentForm class for handling comment form data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Specify the model to be used for the form
        fields = ('body',)  # Specify the fields to be included in the form

# Define ContactForm class for handling contact form data


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  # Specify the model to be used for the form
        # Specify the fields to be included in the form
        fields = ['name', 'email', 'subject', 'message']
