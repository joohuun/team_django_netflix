from django.urls import path
from . import views
# 지금 내가 있는 폴더에서 views라는 파이썬 파일을 가져올거야!

app_name = 'movie'
urlpatterns = [
    #path('', views.csvTomodel, name='csvTomodel'),
    path('', views.home, name='home'),
    path('<int:id>', views.detail, name='detail'),
    path('<int:movie_pk>/likes', views.likes, name='likes'),
]
