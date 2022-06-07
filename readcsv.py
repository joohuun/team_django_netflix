import csv
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "team_django_netflix.settings")
django.setup()

from movie.models import *

CSV_PATH = 'movie.csv'


def insert_movie():
    with open(CSV_PATH, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)
    
        for row in data_reader:
        
            print(row)  
            movie = MovieModel.objects.create(
                            code = row['code'],
                            title = row['title'],
                            age = row['age'],
                            openDate = row['openDate'],
                            rate = row['rate'] if row['rate'] else None,
                            actors = row['actors'],
                            story = row['story'] if row['story'] else None,            
                    )
  
  
insert_movie()
  
  
# with open(CSV_PATH, newline='') as csvfile:
#     rows = csv.reader(csvfile)
#     next(rows, None)
#     for row in rows:
#         print(row[1])
#         MovieModel.objects.create(
#             code = row[0],
#             # title = row[1],
#             # age = row[2],            
#         )
#         # print(row)

