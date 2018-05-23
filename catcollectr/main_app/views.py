"""Views."""
from django.shortcuts import render
from .models import Cat
from .forms import CatForm
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    """Index page."""
    cats = Cat.objects.all()
    form = CatForm()
    return render(request, 'index.html', {'cats': cats, 'form': form})


def show(request, cat_id):
    """Show one cat."""
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'show.html', {'cat': cat})


def post_cat(request):
    """Post cat form."""
    form = CatForm(request.POST)
    if form.is_valid():
        cat = form.save(commit=False)
        cat.save()
    return HttpResponseRedirect('/')
