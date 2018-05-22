"""Views."""
from django.shortcuts import render
from .models import Cat


def index(request):
    """Index page."""
    cats = Cat.objects.all()
    return render(request, 'index.html', {'cats': cats})


def show(request, cat_id):
    """Show one cat."""
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'show.html', {'cat': cat})
