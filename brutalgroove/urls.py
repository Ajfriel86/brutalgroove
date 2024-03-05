# URL configuration guide and example imports for Django's URL routing
# Import the admin module to enable the admin interface
from django.contrib import admin
# Import path for routing and include for including other URLconfs
from django.urls import path, include
from .views import handler404, handler500


# urlpatterns: A list of URL patterns
# to route URLs to their corresponding views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
]


handler404 = 'brutalgroove.views.handler404'
handler500 = 'brutalgroove.views.handler500'
