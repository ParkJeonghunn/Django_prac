from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Article, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

@login_required(login_url='signin')
def new(request):
    if request.method == 'POST':
        article = Article.objects.create(
            author = request.user,
            title = request.POST['title'],
            content = request.POST['content']
        )
        return  redirect('detail', article.pk)
    else:
        return render(request, 'blog/new.html')

@login_required(login_url='sigin')
def detail(request, pk): # 사용자가 어떤 글을 보고자 했는지를 받아줘야하기 때문
    article = Article.objects.get(pk=pk) # 왼쪽의 Pk 필드명으로서의 Pk, 오른쪽 Pk 변수명(user가 넘기는 값)
    return render(request, 'blog/detail.html', {'article':article}) # 왼쪽은 html 에서 쓰는 변수명, 오른쪽은 views의 변수명

@login_required(login_url='siginin')
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.author:
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('detail', article.pk)
    else:
       return render(request, 'blog/edit.html', {'error':'잘못된 접근입니다.'}
