"""Views."""
from django.shortcuts import render
from .models import Cat


# Create your views here.
def index(request):
    """Index page."""
    cats = Cat.objects.all()
    return render(request, 'index.html', {'cats': cats})
