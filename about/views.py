from django.shortcuts import render
from .models import About

def about_view(request):
    """
    Renders the About page using the first About instance.
    If no About instance exists, passes None to the template.
    """
    about = About.objects.first()  # Get the first (and only) About instance, or None
    return render(request, 'about/about.html', {'about': about})
