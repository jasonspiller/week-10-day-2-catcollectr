"""Views."""
from django.shortcuts import render
from .models import Cat
from .forms import CatForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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
        cat.user = request.user
        cat.save()
    return HttpResponseRedirect('/')


def profile(request, username):
    """Show user profile."""
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})


def login_view(request):
    """Login form."""
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
