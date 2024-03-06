from django import forms
from .models import Movie, Rating

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'image']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['name', 'rating']