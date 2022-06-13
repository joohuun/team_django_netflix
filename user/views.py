
from django.shortcuts import redirect, render
from movie.models import GenreModel
from .models import ProfileModel, UserModel
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# user/views.py
# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if password != password2:
            return render(request, 'user/signup.html', {'error':'패스워드를 확인 해주세요'})
        else:
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error':'사용자 이름과 패스워드는 필수 값 입니다.'})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html', {'error':'중복된 이름이 존재 합니다'})  # 중복된 사용자가 있을시 다시 signup 페이지로 이동
            else:
                UserModel.objects.create_user(username=username, password=password)
                return redirect('/create-profile')  


def create_profile(request):
    if request.method == 'GET':
        genre = GenreModel.objects.all()
        return render(request, 'user/createprofile.html', {'genre':genre})
    
    elif request.method == 'POST':
        age = request.POST.get('age', None)  
        profilename = request.POST.get('profilename', None)
        genre_name = request.POST.get('genre', None)        
        genre = GenreModel.objects.get(genre=genre_name)
        profile = ProfileModel.objects.create(profilename=profilename, genre=genre, age=age)
        return redirect('/sign-in', profile.pk)
        
            
            
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error':'유저이름 혹은 패스워드를 확인하세요'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')



@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

##############
def follow(request, username):
    if request.method == 'POST':
        target_user = UserModel.objects.get(username=username)
        user = request.user
        user.following.add(target_user)
        user.save()
        return redirect('/')
    
def view_follow(request):
    if request.method == 'GET':
        user = request.user
        following = list(user.follow.all().values('username'))
        return render(request, 'user/view_follow.html', {'following':following})
    
###############