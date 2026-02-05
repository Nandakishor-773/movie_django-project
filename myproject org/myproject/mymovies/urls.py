from django.urls import path
from .views import movie_list, add_movie, edit_movie

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('add/', add_movie, name='add_movie'),
    path('edit/<int:id>/', edit_movie, name='edit_movie'),
]
