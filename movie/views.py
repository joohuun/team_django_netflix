from django.shortcuts import render, redirect
from django.http import HttpResponse
import re
from urllib import request
import csv

from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
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
# def like_view(request, movie_pk):
#     if request.method == 'get':
#         like_list = LikeModel.objects.filter(user=request.user, movie=movie_pk)
#         return render(request, 'movie/detail.html', {'like_list': like_list})


# # @login_required
# def detail(request):
#     if request.method == 'GET':
#         movies = MovieModel.objects.all().order_by('title')
#         return render(request, 'movie/detail.html', {'movies': movies})
