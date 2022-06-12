from django.shortcuts import redirect, render
from .models import UserModel
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
            return render(request, 'user/signup.html', {'error': '패스워드를 확인 해주세요'})
        else:
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error': '사용자 이름과 패스워드는 필수 값 입니다.'})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                # 중복된 사용자가 있을시 다시 signup 페이지로 이동
                return render(request, 'user/signup.html', {'error': '중복된 이름이 존재 합니다'})
            else:
                UserModel.objects.create_user(
                    username=username, password=password)
                return redirect('/sign-in')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error': '유저이름 혹은 패스워드를 확인하세요'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/sign-in')
