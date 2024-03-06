# Import necessary Django modules and components
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView
from .models import Post, HeroImage, Comment  # Import models
from .forms import CommentForm, ContactForm  # Import form
from django.contrib import messages
from allauth.account.forms import SignupForm
import logging
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div


# Set up logger for this module
logger = logging.getLogger(__name__)


class CombinedHomeView(ListView):
    """
    View to display a list of posts
    """
    model = Post  # Specifies the model to use
    template_name = "home.html"  # Template file to render
    # Context name that will be used in the template
    context_object_name = "post_list"
    paginate_by = 2  # Number of posts per page

    def get_queryset(self):
        """
        Overriding the get_queryset method to return the queryset
        of posts filtered by status.
        """
        return Post.objects.filter(status=1).order_by("-created_on")

    def get_context_data(self, **kwargs):
        """
        Overriding the get_context_data method to add HeroImage objects
        to the context.
        """
        context = super().get_context_data(**kwargs)
        context['hero_images'] = HeroImage.objects.filter(is_active=True)
        return context


class PostDetail(View):
    """
    View to display a single post detail
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Handles POST requests, specifically for submitting comments
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.approved = False
            comment.save()
            messages.success(
                request, "Your comment has been submitted and is awaiting approval.")
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.error(
                request, "There was an error with your comment. Please try again.")
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": comment_form
            },
        )


class PostLike(View):
    """
    View to handle post like functionality
    """

    def post(self, request, slug, *args, **kwargs):
        """
        Toggle like status for a post
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'A member of our team will reach out in due course.')
            return redirect('registration_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


class CustomSignupForm(SignupForm):
    """
    Custom signup form that extends the default allauth 
    SignupForm with django-crispy-forms layout.

    """

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Submit('signup', 'Sign Up', css_class='btn-primary')
        )


class CustomSignupView(SignupView):
    """
    Custom signup view that extends allauth's SignupView
    """
    form_class = CustomSignupForm
    success_url = reverse_lazy('registration_success')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


def comment_delete(request, comment_id):
    """
    View to handle comment deletion
    """
    logger.debug(f"Attempting to delete comment with ID: {comment_id}")
    comment = get_object_or_404(Comment, id=comment_id)
    post_slug = comment.post.slug
    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
        return redirect('post_detail', slug=post_slug)
    else:
        return redirect('post_detail', slug=post_slug)


def custom_error_view(request, error_message=None):
    """
    View to handle custom error
    """
    context = {
        'error_message': error_message or "An unexpected error occurred."
    }

    return render(request, '404.html', context)


@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('post_detail', slug=comment.post.slug)
        else:
            form = CommentForm(instance=comment)
        return render(request, 'comment_edit.html', {'form': form, 'comment': comment})
    else:
        return redirect('post_detail', slug=comment.post.slug)
