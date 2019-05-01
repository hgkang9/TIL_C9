from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title', 'audience', 'poster_url', 'genre','description']