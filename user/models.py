# user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser  # 장고 기본 제공 유저모델


# 유저 회원 테이블
class UserModel(AbstractUser):
    class Meta:
        db_table = "user"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)