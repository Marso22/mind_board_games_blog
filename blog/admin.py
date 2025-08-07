from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'category')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body_excerpt', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'post')
    search_fields = ('author__username', 'body', 'post__title')
    actions = ['approve_comments', 'disapprove_comments']
    
    def body_excerpt(self, obj):
        """Show first 50 characters of comment body"""
        return obj.body[:50] + "..." if len(obj.body) > 50 else obj.body
    body_excerpt.short_description = 'Comment'
    
    def approve_comments(self, request, queryset):
        """Bulk approve selected comments"""
        count = queryset.update(approved=True)
        self.message_user(request, f'{count} comment(s) approved successfully!')
    approve_comments.short_description = "Approve selected comments"
    
    def disapprove_comments(self, request, queryset):
        """Bulk disapprove selected comments"""
        count = queryset.update(approved=False)
        self.message_user(request, f'{count} comment(s) disapproved successfully!')
    disapprove_comments.short_description = "Disapprove selected comments"