# user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser  # 장고 기본 제공 유저모델
from movie.models import GenreModel
from movie.models import MovieModel
from django.conf import settings


AGE_CHOICE = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)


# 유저 회원 테이블
class UserModel(AbstractUser):
    class Meta:
        db_table = "user"

    profiles = models.ManyToManyField('ProfileModel')
    follow = models.ManyToManyField('self', symmetrical=False, blank=True)


# 회원가입 후 프로필 설정 (장르, 닉네임, 나이 설정)
class ProfileModel(models.Model):
    class Meta:
        db_table = "profile"

    profilename = models.CharField(max_length=50)
    genre = models.ForeignKey(
        GenreModel, on_delete=models.CASCADE)  # 장르 한개 밖에 못고름
    age = models.CharField(max_length=5, choices=AGE_CHOICE)
    # genre = models.ManyToManyField(GenreModel, null=True) # 오류남

    def __self__(self):
        return self.age + "" + self.profilename + "" + self.genre
