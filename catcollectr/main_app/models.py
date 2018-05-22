"""Models."""
from django.db import models


class Cat(models.Model):
    """Cat class."""

    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        """Output name."""
        return self.name
