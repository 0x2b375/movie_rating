from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Rating
from django.db.models import Avg, Count
from .forms import MovieForm, RatingForm
from django.db.models import Q
from django.contrib import messages
# Create your views here.


def movie_list(request):
    movies = Movie.objects.annotate(
        avg_rating=Avg('rating__rating'),
        total_ratings=Count('rating')
    )
    return render(request, 'ratings/movie_list.html', {'movies': movies})


def add_rating(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rating_value = form.cleaned_data['rating']

            existing_rating = Rating.objects.filter(
                movie=movie, name=name).exists()
            if existing_rating:
                messages.warning(
                    request, f"A rating by the name '{name}' already exists for this movie.")
                return redirect('add_rating', movie_id=movie_id)

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


def delete_rating(request, rating_id):

    rating = get_object_or_404(Rating, id=rating_id)
    if request.method == 'POST':
        rating.delete()
        return redirect('view_ratings', movie_id=rating.movie.id)


def edit_rating(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)
    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            return redirect('view_ratings', movie_id=rating.movie.id)
    else:
        form = RatingForm(instance=rating)
    return render(request, 'ratings/edit_rating.html', {'form': form, 'rating': rating})

def search_feature(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        movies = Movie.objects.filter(title__contains=search_query).annotate(
            avg_rating=Avg('rating__rating'),
            total_ratings=Count('rating')
        )
        return render(request, 'ratings/search_list.html', {'query': search_query, 'movies': movies})
    else:
        return render(request, 'ratings/search_list.html', {})

