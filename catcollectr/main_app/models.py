"""Models."""
from django.db import models
from django.contrib.auth.models import User


class Cat(models.Model):
    """Cat class."""

    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        """Output name."""
        return self.name
