# movie/urls.py
from django.urls import path  # sns/urls.py 연동
from . import views  # 같은 폴더내 views.py 연동

urlpatterns = [
    path('home', views.home, name='home'),
]