from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('add/', views.add_movie, name='add_movie'),
    path('rate/<int:movie_id>/', views.add_rating, name='add_rating'),
    path('ratings/<int:movie_id>/', views.view_ratings, name='view_ratings'),
    path('movies/<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),
]
