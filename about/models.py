"""
Model definition for the About page.
Stores title, content, and last updated timestamp.
"""

from django.db import models

class About(models.Model):
    """
    Represents the About page for Mind Board Games Blog.
    Stores the page title, content, and last updated time.
    """
    title = models.CharField(max_length=200, default="About Mind Board Games")
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"
    
    def __str__(self):
        return self.title
