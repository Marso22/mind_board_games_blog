from django.shortcuts import render
from .models import About

def about_view(request):
    try:
        about = About.objects.first()  # Get the first (and only) About instance
    except About.DoesNotExist:
        about = None
    
    return render(request, 'about/about.html', {'about': about})
