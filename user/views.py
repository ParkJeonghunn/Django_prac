from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # form 태그 요청일때
        # 회원가입 + 로그인
        # 만약 아이디가 중복이라면?
        found_user = User.objects.filter(username=request.POST['username'])
        if len(found_user) > 0:
            return render(request, 'user/siginup.html', {'error':'username이 이미 존재합니다.'})
        else:
            new_user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )
        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user)
        return redirect('index')
    else:
        # 그냥 링크타고 들어왔을 때
        # 회원가입 정보 입력하는 페이지를 보여줘
        return render(request, 'user/siginup.html')

def signin(request):
    if request.method == 'POST':
        # 로그인
        found_user = auth.authenticate(request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is not None:
            auth.login(request, found_user)
            return redirect('index')
        else:
            return render(request, 'user/signin.html', {'error': '유저가 존재하지 않습니다.'})
    else:
        # 로그인 정보 입력하는 페이지를 보여줘
        return render(request, 'user/signin.html')

@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    return redirect('index')