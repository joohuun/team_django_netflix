from re import T
from django.db import models
# from user.models import UserModel


# 장르 모델
class GenreModel(models.Model):
    class Meta:
        db_table = 'genre'

    def __str__(self):
        return self.genre_name

    genre_name = models.CharField(max_length=50, null=True)


class MovieModel(models.Model):
    class Meta:
        db_table = "movie"

    title = models.CharField(max_length=256, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    imgurl = models.CharField(max_length=256, blank=True, null=True)
    age = models.CharField(max_length=256, blank=True, null=True)
    runningtime = models.CharField(max_length=256, blank=True, null=True)
    opendate = models.CharField(max_length=256, blank=True, null=True)
    actors = models.CharField(max_length=256, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    story = models.TextField(blank=True, null=True)


# class LikeModel(models.Model):
#     class Meta:
#         db_table = "like"

#     user = models.ForeignKey('user.UserModel', on_delete=models.CASCADE)
#     movie = models.ForeignKey('movie.MovieModel', on_delete=models.CASCADE)
#     like = models.BooleanField(default=False)
