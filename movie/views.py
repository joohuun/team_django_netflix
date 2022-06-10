from django.shortcuts import render, redirect
from django.http import HttpResponse
import re
from urllib import request
import csv

from .models import *
from django.contrib.auth.decorators import login_required
from . import recommender_ml

# Create your views here.
@login_required
def home(request):
    if request.method == 'GET':
        movies = MovieModel.objects.all().order_by('title')             
        return render(request, 'movie/home.html', {'movies':movies})


# 영화 추천 리스트 (1차 작성 - DB 형태(json?) 알아보고, 영화 id들어있는지 확인)
def recommend_movies(request, pk):
    # return 리스트 불러오기
    recommend = recommender_ml.similarmovies
    movies = recommend.content_based(pk)
    return render(request, 'movie/detail.html', {'movies': movies})

