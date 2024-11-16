from django import forms
from .models import Book

class ExampleForm(forms.form):
    query = forms.CharField(max_length=100)

    