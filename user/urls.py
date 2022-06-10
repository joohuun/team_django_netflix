# user/urls.py
from django.urls import path  # sns/urls.py 연동
from . import views  # 같은 폴더내 views.py 연동

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('logout/', views.logout, name='logout'),
]
