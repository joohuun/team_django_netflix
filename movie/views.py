import re
from urllib import request
from django.shortcuts import redirect, render
import csv

from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    if request.method == 'GET':
        movie = MovieModel.objects.all().order_by('rate')                
        return render(request, 'movie/movielist.html', {'movie':movie})
        
    
    
    
# CSV_PATH = '2022.csv'

# with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
# 	data_reader = csv.DictReader(csvfile)
# 	for row in data_reader:
# 		print(row)
# 		MovieModel.objects.create(
#                          code = row[1],
#                          title = row[2],
        #                  age = row['age'],
        #                  openDate = row['openDate'],
        #                  rate = row['rte'],                                                 
                #   )    
  
    
# import csv

# CSV_PATH = '2022.csv'

# with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
# 	data_reader = csv.DictReader(csvfile)
# 	for row in data_reader:
# 		print(row)
  
# data = []
# for i in range(len()):
#     st = 
  
  
  
# 		MovieModel.objects.create(
#                          code = row['code'],
#         #                  title = row['title'],
#         #                  age = row['age'],
#         #                  openDate = row['openDate'],
#         #                  rate = row['rate'],                                                 
#                   )
  
  
  


    