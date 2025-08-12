from django.urls import path
from . import views

urlpatterns = [
    # Home page and post list
    path('', views.PostList.as_view(), name='home'),

    # Post detail and comment submission
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),

    # Edit a comment (only by author)
    path('posts/<slug:slug>/edit/<int:comment_id>/', views.comment_edit, name='comment_edit'),

    # Delete a comment (only by author)
    path('posts/<slug:slug>/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),

    # Test message view for toast notification
    path('test-message/', views.test_message, name='test_message'),
]