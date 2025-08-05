from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    
    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Post.objects.filter(category=category, status=1).order_by('-created_at')
        return Post.objects.filter(status=1).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Post.CATEGORY_CHOICES
        context['selected_category'] = self.request.GET.get('category')
        return context
