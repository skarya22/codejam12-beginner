from django.http import HttpResponse
from django.shortcuts import render, redirect

from movie.filters import MovieFilter
from movie.forms import MovieForm

from . models import Movie

# Create your views here.
def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    try:
        image = movie.cover.url
    except ValueError:
        image = None

    context = {'movie': movie, 'image': 'False' if image == None else 'True'}
    return render(request, 'movie/detail.html', context)

def list(request):
    movies = Movie.objects.all()
    movie_filter = MovieFilter(request.GET, queryset=movies)
    movies = movie_filter.qs

    context = {'movies_list': movies, 'movie_filter': movie_filter}

    return render(request, 'movie/list.html', context)

def add(request):
    form = MovieForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('list')

    return render(request, 'movie/add.html', context)
