from re import T
from django.db import models



# 장르 모델 
class GenreModel(models.Model):
    class Meta:
        db_table = 'genre'
        
    def __str__(self):
        return self.genre
        
    genre = models.CharField(max_length=50, null=True)



class MovieModel(models.Model):
    class Meta:
        db_table = "movie"
        
    title = models.CharField(max_length=50)
    movie_genre = models.ManyToManyField(GenreModel)
    user_rate = models.FloatField()
    movie_rate = models.FloatField(null=True)
    post_img = models.ImageField()
    actor = models.CharField(max_length=256)
    desc = models.TextField(null=True)