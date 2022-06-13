from django.db import models
from django.conf import settings

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
    genre = models.ManyToManyField(GenreModel)
    age = models.CharField(max_length=256, blank=True, null=True)
    runningtime = models.CharField(max_length=256, blank=True, null=True)
    opendate = models.CharField(max_length=256, blank=True, null=True)
    actors = models.CharField(max_length=256, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    story = models.TextField(blank=True, null=True)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE, default='')
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_articles', blank=True, null=True)

    def __str__(self):
        return self.title
