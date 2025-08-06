from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200, default="About Mind Board Games")
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"
    
    def __str__(self):
        return self.title
