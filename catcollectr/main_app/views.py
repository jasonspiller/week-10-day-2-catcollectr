"""Views."""
from django.shortcuts import render


# Create your views here.
def index(request):
    """Index page."""
    return render(request, 'index.html', {'cats': cats})


class Cat:
    """Cat class."""

    def __init__(self, name, breed, description, age):
        """Cat class constructor."""
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age


cats = [
    Cat('Lolo', 'tabby', 'foul little demon', 3),
    Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Cat('Raven', 'black tripod', '3 legged cat', 4)
]
