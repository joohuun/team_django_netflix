## 1. insert jsonfile
import json

# # 2. insert csvfile  
# import csv   
# import os                         
# import django  
# import sys


########################
## 1. insert jsonfile ##
########################


genre_list = ["미스터리", "공포", "멜로·로맨스", "뮤지컬", "드라마", "액션", "블록버스터", "범죄", "스릴러", "어드벤처",
              "공포", "SF", "가족", "다큐멘터리", "서부", "실화", "애니메이션", "느와르", "판타지", "코미디", "전쟁"]


with open('movie_data.json', 'r', encoding='utf-8') as f:
    movies = json.load(f)
    # print(movies)

new_list = []
for movie in movies:
    new_data = {"model":"movie.moviemodel"}  
    print(movie)
    if movie["genre"]:   ###########
        genres = movie["genre"].strip("[]").split(',')
        genre_int_list = []
        for genre in genres:
            genre_int = genre_list.index(genre.strip()) + 1
            genre_int_list.append(genre_int)
            print(genre_int_list)
        movie['genre'] = genre_int_list
    else:
        movie["genre"] = []
    new_data["fields"] = movie
    new_list.append(new_data)
            
    
with open('movie_data.json', 'w', encoding='utf-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
    
    
############################################################################

   
#     new_data["fields"] = {}  ##########
#     new_data["fields"] = movie
#     new_list.append(new_data)
    
# print(new_list)

# with open('movie_data.json', 'w', encoding='utf-8') as f:
#     json.dump(new_list, f, ensure_ascii=False, indent=2)

    # print("movie=", end=""), print(type(movie))
    # print("movie genre = ",end=""), print(movie.get('genre'))
    # print("movie = ",end=""), print(movie)

            
 
########################
## 2. insert csvfile  ##
########################


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "team_django_netflix.settings")
# django.setup()

# from movie.models import *

# CSV_PATH = './movie.csv'

# def insert_movie():
#     with open(CSV_PATH, newline='', encoding="utf-8") as csvfile:
#         data_reader = csv.DictReader(csvfile)
#         for row in data_reader:
#             movie = MovieModel.objects.create(
#                             title = row['title'],
#                             url = row['url'],
#                             imgurl = row['imgurl'] if row['imgurl'] else None,
#                             genre = row['genre'] if row['genre'] else None,
#                             age = row['age'] if row['age'] else None,
#                             runningtime = row['runningtime'] if row['runningtime'] else None,
#                             opendate = row['opendate'] if row['opendate'] else None,
#                             actors = row['actors'] if row['actors'] else None,
#                             rate = row['rate'] if row['rate'] else None,                            
#                             story = row['story'] if row['story'] else None,
#                     )
#             print(movie)  
# insert_movie()
  

  





