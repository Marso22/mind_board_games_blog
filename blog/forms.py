from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    Form for submitting and editing comments on blog posts.
    Uses a textarea widget with custom styling and placeholder.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your thoughts about this board game...',
                'rows': 4
            })
        }
        labels = {
            'body': 'Your Comment'
        }