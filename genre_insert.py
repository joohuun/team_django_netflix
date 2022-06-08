import json

with open('genre.json','r', encoding='utf-8') as f:
    genre_list = json.load(f)
print(genre_list)
    
new_list = []
for genre in genre_list:
    new_data = {"model": "movie.genremodel"}   # appname.modelname
    new_data["fields"] = {}
    new_data["fields"]["genre_name"] = genre
    new_list.append(new_data)
    
print(new_list)

with open('genre_data.json', 'w', encoding='utf-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
