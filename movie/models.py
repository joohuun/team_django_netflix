from django.db import models



# 장르 모델 
class GenreModel(models.Model):
    class Meta:
        db_table = 'genre'
        
    # def __str__(self):
    #     return self.genre
        
    genre_name = models.CharField(max_length=256, default='')



class MovieModel(models.Model):
    class Meta:
        db_table = "movie"
        
    title = models.CharField(max_length=256, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    imgurl = models.CharField(max_length=256, blank=True, null=True)
    genre = models.ManyToManyField(GenreModel, related_name='moviemodels')
    age = models.CharField(max_length=256, blank=True, null=True)
    runningtime = models.CharField(max_length=256, blank=True, null=True)
    opendate = models.CharField(max_length=256, blank=True, null=True)
    actors = models.CharField(max_length=256, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    # post_img = models.ImageField(upload_to='upload', height_field=None, width_field=None, blank=True, null=True)    