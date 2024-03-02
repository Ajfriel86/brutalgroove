# Standard import statements for Django settings
import os
import sys
from pathlib import Path
from django.contrib.messages import constants as messages
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api


# Load environment variables from `env.py` if it exists
if os.path.isfile("env.py"):
    import env

# Define the base directory for the project and the directory for templates
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Security settings: SECRET_KEY for cryptographic signing,
# DEBUG mode setting, and allowed hosts for HTTP requests
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = 'False'

ALLOWED_HOSTS = [
    'brutalgroove-1df729525c70.herokuapp.com',
    'localhost',
    '127.0.0.1',
]


# Definition of installed apps, including Django's default apps and
# additional packages like allauth and cloudinary
INSTALLED_APPS = [
    # Default Django apps for admin, auth, sessions, etc.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    # Third-party apps for authentication and media storage
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    # UI enhancement apps
    'crispy_bootstrap5',
    'crispy_forms',
    'django_summernote',
    # Custom blog app
    'blog',
]

SITE_ID = 1

# URL redirection settings post-login and logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Message tags for bootstrap alerts
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Middleware configuration for handling requests, sessions, security, etc.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'brutalgroove.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Remove email confirmation from allauth
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False

WSGI_APPLICATION = 'brutalgroove.wsgi.application'


# Database configuration, using dj_database_url
# for parsing DATABASE_URL from environment variables
if "DEVELOPMENT" in os.environ:
    print('development environment')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        },
    }
else:
    print('production environment')
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }

# Database for testing
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'rntxdypg',  # Your database name
#         'USER': 'rntxdypg',  # Your database username
#         'PASSWORD': 'hVEtA75OJkYLgPsn5H4KXKHHLwZ34s7t',
#         'HOST': 'trumpet.db.elephantsql.com',
#         'PORT': '5432',  # Default PostgreSQL port
#         'OPTIONS': {
#             'sslmode': 'require',
#         },
#     }
# }

# Credentials for database for testing
if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Cloudinary settings
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET"),
)

# Static and media files configuration, including URLs and storage backends
STATIC_URL = '/static/'
STATICFILES_STORAGE = (
    'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
)
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Crispy forms configuration for Bootstrap 5
CRISPY_TEMPLATE_PACK = 'bootstrap5'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
