# user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser  # 장고 기본 제공 유저모델
from movie.models import GenreModel



AGE_CHOICE = (
    ('All', 'All'),
    ('Kids', 'Kids'),   
)


# 유저 회원 테이블
class UserModel(AbstractUser):
    class Meta:
        db_table = "user"

    profiles = models.ManyToManyField('ProfileModel')
    
    
# 회원가입 후 프로필 설정 (장르, 닉네임, 나이 설정)
class ProfileModel(models.Model):
    class Meta:
        db_table = "profile"
        
    profilename = models.CharField(max_length=50)  
    genre_name = models.ForeignKey(GenreModel, on_delete=models.CASCADE, null=True) # 장르 한개 밖에 못고름
    age = models.CharField(max_length=5, choices=AGE_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    # genre_name = models.ManyToManyField(GenreModel, related_name='prifiles') # 오류남 장르 3개 까지 골르려고 했으나 오류

      
    def __self__(self):
        return self.age +""+ self.profilename +""+ self.genre 
    
    

        
        
    