from . import views  # Import views module
from django.urls import path  # Import path function from django.urls module
from .views import *  # Import all views from views module
from .views import CustomSignupView  # Import CustomSignupView from views module
from django.conf import settings  # Import settings from django.conf module
# Import static function from django.conf.urls.static module
from django.conf.urls.static import static
# Import TemplateView from django.views.generic module
from django.views.generic import TemplateView
# Import comment_delete function from views module
from .views import comment_delete

# Define urlpatterns, a list of URL patterns
urlpatterns = [

    path('', views.CombinedHomeView.as_view(), name='home'),
    path('contact/', contact_view, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('comment/<int:comment_id>/delete/',
         comment_delete, name='comment_delete'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('registration/success/', TemplateView.as_view(
        template_name='registration_success.html'), name='registration_success'),
    path('custom-error/', views.custom_error_view, name='custom_error_view'),
]
