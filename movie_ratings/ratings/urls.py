from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero_section, name='hero_section'),
    path('movie-list', views.movie_list, name='movie_list'),
    path('add', views.add_movie, name='add_movie'),
    path('rate/<int:movie_id>', views.add_rating, name='add_rating'),
    path('ratings/<int:movie_id>', views.view_ratings, name='view_ratings'),
    path('movies/<int:movie_id>/delete',
         views.delete_movie, name='delete_movie'),
    path('delete_rating/<int:rating_id>',
         views.delete_rating, name='delete_rating'),
    path('edit-rating/<int:rating_id>', views.edit_rating, name='edit_rating'),
    path('search', views.search_feature, name='search-view'),
]
