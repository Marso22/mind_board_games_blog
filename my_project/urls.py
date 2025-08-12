"""
URL configuration for mind_board_games_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from blog.views import CustomSignupView

urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),

    # Custom signup view for user registration
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),

    # Main blog app URLs (home, posts, comments)
    path('', include('blog.urls')),

    # About page URLs
    path('about/', include('about.urls')),

    # Django Allauth authentication URLs
    path('accounts/', include('allauth.urls')),

    # Summernote rich text editor URLs
    path("summernote/", include("django_summernote.urls")),
]