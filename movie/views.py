from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import *
from . import recommender_ml
from . import collab_recommender
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# 메인페이지
@login_required
def home(request):
    if request.method == 'GET':
        #collab_recommender();
        # 전체 다불러옴
        movies = MovieModel.objects.all().order_by('-pk')
        infos = {}
        genre_list = []
        for movie in movies:
            genres = movie.genre.all()
            infos[movie] = genres
        # print(infos)
        
        # 찜한 컨텐츠
        user = request.user
        user_like = list(user.like_movie.all())
        likes = {}
        for like in user_like:
            genre = like.genre.all()
            likes[like] = genre

        # 평점 별 줄세우기
        rate_ranking = MovieModel.objects.all().order_by('-rate')[:21]
        ranking = {}
        rate_genres = []
        for rank in rate_ranking:
            genre = rank.genre.all()
            ranking[rank] = genre

        return render(request, 'movie/home.html', {'infos': infos, 'likes':likes, 'ranking':ranking})


# 상세페이지 중, 하
@login_required
def recommend_movies(request, pk):
    if request.method == "GET":
        # 상
        movie_detail = MovieModel.objects.get(pk=pk)
        print("movie_detail: ", movie_detail)
        # 중 - 댓글
        page = request.GET.get('page', 1)
        comment_list = MovieComment.objects.filter(
            movie=pk).order_by('-created_at')

        paginator = Paginator(comment_list, 3)
        comments = paginator.get_page(page)

        # 하 - 추천
        recommend = recommender_ml.similarmovies
        movies = recommend.content_based(pk-1)
        infos ={}
        for movie in movies:
            genres = movie.genre.all()
            infos[movie] = genres
    
        return render(request, 'movie/detail.html', {'movie':movie_detail,'infos': infos, 'comment_list': comments})


# 댓글 작성
@login_required
def comment_create(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment", "")
        rate = request.POST.get("user_rate", "")

        # user = TestUser.objects.get(id=id)
        movie = MovieModel.objects.get(pk=id)

        comment_db = MovieComment()
        comment_db.user = request.user
        comment_db.movie = movie
        comment_db.comment = comment
        comment_db.user_rate = rate
        comment_db.save()

        return redirect("/"+str(id))


# 댓글 삭제
@login_required
def comment_delete(request,pk, id):
    comment = MovieComment.objects.get(id=id)
    #comment_id = comment.movie_id.id
    comment.delete()

    return redirect('/' + str(pk))


# 좋아요
@csrf_exempt
def like(request, pk):
    if request.method=="POST":
        movie = MovieModel.objects.get(pk=pk)
        movie.like_user.add(request.user)
        movie.save()
        print("완료")
        return redirect("/")

    # elif request.method =="GET":
    #     movie = MovieModel.objects.get(pk=pk)
    #     likes = list(movie.like_user.all().values('user'))
    #     print(likes)
    #     return JsonResponse({'status':likes})