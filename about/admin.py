"""
Admin configuration for the About app.
Customizes admin interface for the About model.
"""

from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface for About model with Summernote integration.
    Only allows a single About instance.
    """
    summernote_fields = ('content',)
    list_display = ('title', 'updated_at')
    
    def has_add_permission(self, request):
        # Only allow one About instance in the admin
        return not About.objects.exists()
