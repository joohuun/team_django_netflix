from turtle import ondrag
from django.db import models
from user.models import UserModel
from django.conf import settings


COMMENT_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ('6', 6),
    ('7', 7),
    ('8', 8),
    ('9', 9),
    ('10', 10),
)


# 장르 모델
class GenreModel(models.Model):
    class Meta:
        db_table = 'genre'

    def __str__(self):
        return self.genre_name

    genre_name = models.CharField(max_length=50, null=True)


# 영화 정보 DB
class MovieModel(models.Model):
    class Meta:
        db_table = "movie"

    title = models.CharField(max_length=256, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    imgurl = models.CharField(max_length=256, blank=True, null=True)
    genre = models.ManyToManyField(GenreModel, related_name='genre')
    age = models.CharField(max_length=256, blank=True, null=True)
    runningtime = models.CharField(max_length=256, blank=True, null=True)
    opendate = models.CharField(max_length=256, blank=True, null=True)
    actors = models.CharField(max_length=256, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie', blank=True)


# 영화 댓글 모델
class MovieComment(models.Model):
    class Meta:
        db_table = 'comment'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    user_rate = models.CharField(max_length=5, choices=COMMENT_POINT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment



