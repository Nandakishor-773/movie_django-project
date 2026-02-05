from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

@login_required
def add_movie(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        movie = form.save(commit=False)
        movie.user = request.user
        movie.save()
        return redirect('movie_list')
    return render(request, 'add_movie.html', {'form': form})

@login_required
def edit_movie(request, id):
    movie = get_object_or_404(Movie, id=id, user=request.user)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movie_list')
    return render(request, 'edit_movie.html', {'form': form})

