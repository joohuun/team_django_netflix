from distutils.command.upload import upload
from re import T
from tkinter.tix import Tree
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
        
    code = models.IntegerField()
    title = models.CharField(max_length=100)
    genre = models.ManyToManyField(GenreModel)
    age = models.CharField(max_length=100)
    openDate = models.CharField(max_length=100, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    participate = models.FloatField(blank=True, null=True)
    actors = models.CharField(max_length=256, blank=True)
    story = models.TextField(blank=True, null=True)
    post_img = models.ImageField(upload_to='upload', height_field=None, width_field=None, blank=True, null=True)    