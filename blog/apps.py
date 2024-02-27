from django.apps import AppConfig

# Define the configuration for the 'blog' app


class BlogConfig(AppConfig):
    # Set the default primary key field for models to BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    # Set the name of the app
    name = 'blog'
