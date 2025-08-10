from django.urls import path
from . import views
from .views import CustomSignupView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('posts/<slug:slug>/edit_comment/<int:comment_id>/', 
         views.comment_edit, name='comment_edit'),
    path('posts/<slug:slug>/delete_comment/<int:comment_id>/', 
         views.comment_delete, name='comment_delete'),
#    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
]