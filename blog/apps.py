from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Set the default primary key field for models to BigAutoField
    """
    default_auto_field = 'django.db.models.BigAutoField'
    # Set the name of the app
    name = 'blog'
