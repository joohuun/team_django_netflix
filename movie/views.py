from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
import re
from urllib import request
import csv

from .models import *
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == 'GET':
        movies = MovieModel.objects.all().order_by('title')
        return render(request, 'movie/home.html', {'movies': movies})


@login_required
def detail(request, id):
    movie = MovieModel.objects.get(pk=id)
    return render(request, 'movie/detail.html', {'movie': movie})

# @login_required
# def detail(request):
#     if request.method == 'GET':
#         movies = MovieModel.objects.all().order_by('title')
#         return render(request, 'movie/detail.html', {'movies': movies})


@login_required
def likes(request, movie_pk):
    movie = get_object_or_404(MovieModel, pk=movie_pk)

    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movie:detail', movie_pk)
