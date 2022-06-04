# user/models.py
import profile
from django.db import models
from django.contrib.auth.models import AbstractUser  # 장고 기본 제공 유저모델
from movie.models import GenreModel



GENRE_CHOICE = (
    ('action', 'action'),
    ('romance', 'romance'),   
)


# 유저 회원 테이블
class UserModel(AbstractUser):
    class Meta:
        db_table = "user"

    profiles = models.ManyToManyField('ProfileModel')
    

# 회원가입 후 프로필 설정 (장르, 닉네임 설정)
class ProfileModel(models.Model):
    class Meta:
        db_table = "profile"
        
    name = models.CharField(max_length=50)  
    genre = models.ForeignKey(GenreModel, choices=GENRE_CHOICE, null=True, on_delete=models.CASCADE)
    
    def __self__(self):
        return self.name + "" + self.prefer_genre
    
    

        
        
    