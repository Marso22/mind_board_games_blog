from django.urls import path
from . import views

# URL patterns for the About app
urlpatterns = [
    # About page view
    path('', views.about_view, name='about'),
]