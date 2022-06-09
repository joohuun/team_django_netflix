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
