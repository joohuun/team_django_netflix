import csv
import os
import django
import openpyxl


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "team_django_netflix.settings")
django.setup()

from movie.models import *

CSV_PATH = 'moviedata.csv'


def insert_movie():
    with open(CSV_PATH, newline='', encoding="utf-8") as csvfile:
        data_reader = csv.DictReader(csvfile)
    
        for row in data_reader:
        
            print(row)  
            movie = MovieModel.objects.create(
                            title = row['title'],
                            url = row['url'],
                            imgurl = row['imgurl'],
                            # genre = row['genre'],
                            runningtime = row['runningtime'] if row['runningtime'] else None,
                            opendate = row['opendate'] if row['opendate'] else None,
                            rate = row['rate'] if row['rate'] else None,                            
                            actors = row['actors'] if row['actors'] else None,
                            age = row['age'],
                            story = row['story'] if row['story'] else None,
                    )
            print(movie)  
insert_movie()
  
  
  
# wb = openpyxl.load_workbook('cine21.xlsx')
# sheet1 = wb['Sheet1']
# rows = sheet1['A2':'I336']

    
# for row in rows:
#     print(row)  
#     movie = MovieModel.objects.create(
#                     title = row[0],
#                     url = row[1],
#                     imgurl = row[2],
#                     genre_name = row[3] if row[3] else None,
#                     runningtime = row[4],
#                     opendate = row[5],
#                     actors = row[6],
#                     age = row[7],
#                     story = row[8] if row[8] else None,
#             )




