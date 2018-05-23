"""Forms."""
from django import forms
from .models import Cat


class CatForm(forms.ModelForm):
    """Cat form class."""

    class Meta:
        """Since the model is exactly like the form, use Meta."""

        model = Cat
        fields = ['name', 'breed', 'description', 'age']
