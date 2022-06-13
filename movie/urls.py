from django.urls import path
from . import views
# 지금 내가 있는 폴더에서 views라는 파이썬 파일을 가져올거야!


# urlpatterns = [
#      path('home/', views.home, name='home'), #메인페이지
#      path('<int:pk>', views.recommend_movies, name='recommend_movies'),
#      path('movie/comment/create/<int:id>',
#          views.comment_create, name='comment-create'),
#      path('<int:pk>/comment/delete/<int:id>',
#          views.comment_delete, name='comment-delete'),
#      path('<int:movie_pk>/likes', views.likes, name='likes'),
# ]

app_name = "movie"

urlpatterns = [ 
    path('', views.main, name='main'), 
    path('home/', views.home, name='home'), 
    path('<int:pk>', views.recommend_movies, name='recommend_movies'), 
    path('movie/comment/create/<int:id>', views.comment_create, name='comment-create'), 
    path('<int:pk>/comment/delete/<int:id>', views.comment_delete, name='comment-delete'), 
    path('<int:pk>/likes', views.likes, name="likes"), 
    path('search/', views.search, name="search"), ]