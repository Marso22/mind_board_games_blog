from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'updated_at')
    
    def has_add_permission(self, request):
        # Only allow one About instance
        return not About.objects.exists()
