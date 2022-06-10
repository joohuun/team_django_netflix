from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import *
from . import recommender_ml


# Create your views here.
@login_required
def home(request):
    if request.method == 'GET':

        movies = MovieModel.objects.all().order_by('pk')
        return render(request, 'movie/home.html', {'movies': movies})


# 상세페이지 중, 하
def recommend_movies(request, pk):
    recommend = recommender_ml.similarmovies
    movies = recommend.content_based(pk)

    page = request.GET.get('page', 1)
    comment_list = MovieComment.objects.filter(
        movie=id).order_by('-created_at')

    paginator = Paginator(comment_list, 3)
    comments = paginator.get_page(page)

    return render(request, 'movie/detail.html', {'movies': movies, 'comment_list': comments})


# 댓글 작성
@login_required
def comment_create(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment", "")
        rate = request.POST.get("rate", "")

        # user = TestUser.objects.get(id=id)
        movie = MovieModel.objects.get(id=id)

        comment_db = MovieComment()
        comment_db.user = request.user
        comment_db.movie = movie
        comment_db.comment = comment
        comment_db.user_rate = rate

        return redirect('/comment/' + str(id))


# 댓글 삭제
@login_required
def comment_delete(request, id):
    comment = MovieComment.objects.get(id=id)
    comment_id = comment.movie_id.id
    comment.delete()

    return redirect('/comment/' + str(comment_id))
