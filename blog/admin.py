# Importing necessary modules and models from Django and django-summernote
from django.contrib import admin
# Importing the Post, Comment, and HeroImage models from the current app
from .models import Post, Comment, HeroImage
# Importing SummernoteModelAdmin for rich text editing
from django_summernote.admin import SummernoteModelAdmin

# Admin configuration for the Post model


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Display these fields in the admin list view
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    # Fields to include in the admin search functionality
    search_fields = ['title', 'content']
    # Enable filtering by these fields in the admin
    list_filter = ('status', 'created_on')
    # Automatically generate the slug from the title field
    prepopulated_fields = {'slug': ('title',)}
    # Specify fields to use the Summernote rich text editor
    summernote_fields = ('content',)

# Admin configuration for the Comment model


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Display these fields in the admin list view
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    # Enable filtering by these fields in the admin
    list_filter = ('approved', 'created_on')
    # Fields to include in the admin search functionality
    search_fields = ('name', 'email', 'body')
    # Custom action to approve comments
    actions = ['approve_comments']

    # Method to approve comments
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

# Admin configuration for the HeroImage model


@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    """
    Display these fields in the admin list view
    """
    list_display = ('title', 'is_active', 'created_at')
    # Enable filtering by these fields in the admin
    list_filter = ('is_active', 'created_at')
    # Fields to include in the admin search functionality
    search_fields = ('title', 'caption')
