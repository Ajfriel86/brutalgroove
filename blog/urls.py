from . import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


# Define urlpatterns, a list of URL patterns
urlpatterns = [
    path('', views.CombinedHomeView.as_view(), name='home'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact_success'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('comment/<int:comment_id>/edit/', comment_edit, name='comment_edit'),
    path(
        'comment/<int:comment_id>/delete/', comment_delete, name='comment_delete'
    ),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('registration/success/', TemplateView.as_view(
        template_name='registration_success.html'), name='registration_success'),
]
