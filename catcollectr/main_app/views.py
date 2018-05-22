"""Views."""
from django.http import HttpResponse


# Create your views here.
def index(self):
    """Index page."""
    return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')
