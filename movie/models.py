from django.db import models
from user.models import ProfileModel


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


class MovieComment(models.Model):
    user_id = models.ForeignKey(TestUser, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(TestMovie, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    user_rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment