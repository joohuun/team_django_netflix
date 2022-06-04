# user/models.py
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
        
    profilename = models.CharField(max_length=225)  
    genre = models.ManyToManyField(GenreModel, null=True)
    
    def __self__(self):
        return self.profilename + "" + self.genre
    
    

        
        
    