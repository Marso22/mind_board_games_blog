from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField  # ← Comment out temporarily

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('classic', 'Classic mind board games'),
        ('strategy', 'Strategy mind board games'),
        ('apps', 'Mind board games apps'),
    ]
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='classic',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    rating = models.FloatField(default=0.0)
    featured_image = models.ImageField(upload_to='images/', blank=True, null=True)  # Temporary ImageField
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
       return f"{self.title} | written by {self.author}"



class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name="comments"
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
