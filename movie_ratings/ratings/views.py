from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Rating
from .forms import MovieForm, RatingForm
# Create your views here.


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'ratings/movie_list.html', {'movies': movies})


def add_rating(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.movie = movie
            rating.save()
            return redirect('movie_list')
    else:
        form = RatingForm()
    return render(request, 'ratings/add_rating.html', {'form': form, 'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'ratings/add_movie.html', {'form': form})


def view_ratings(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    ratings = Rating.objects.filter(movie=movie)
    return render(request, 'ratings/view_ratings.html', {'movie': movie, 'ratings': ratings})


def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':

        movie.delete()
        return redirect('movie_list')
