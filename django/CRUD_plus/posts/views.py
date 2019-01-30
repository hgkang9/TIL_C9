from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

#def throw
#def catch
def new(request):
    return render(request, 'new.html')

def create(request):
    # request.GET / request.POST
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    #DB insert
    post = Post(title=title, content=content)
    post.save()
    
    return redirect(f'/posts/{post.pk}/') #post 요청이므로 다른 페이지로 리턴함
    
def index(request):
    
    #all post
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts':posts})
    
def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post':post})
    
def naver(request, q):
    return redirect(f'https://search.naver.com/search.naver?query={q}')
    
def github(request, username):
    return redirect(f'https://github.com/{username}')
    
def delete(request, post_id):
    # 삭제하는 코드
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/posts/')
    
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post':post})
    
def update(request, post_id):
    # 수정하는 코드
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect(f'/posts/{post_id}')
    
