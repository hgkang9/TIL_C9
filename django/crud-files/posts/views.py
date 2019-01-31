from django.shortcuts import render, redirect
from .models import Post, Comment

# Create your views here.

#def throw
#def catch
def new(request):
    return render(request, 'new.html')

def create(request):
    # request.GET / request.POST
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.FILES.get('image') #(이미지)파일 방식이기 때문에 FILES로 받는다
    
    #DB insert
    post = Post(title=title, content=content, image=image)
    post.save()
    
    return redirect('posts:detail', post.pk) #post 요청이므로 다른 페이지로 리턴함 / app_name:넘겨줄 url_name , 동적변수
    
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
    return redirect('posts:list') # app_name : url_name
    
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post':post})
    
def update(request, post_id):
    # 수정하는 코드
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect('posts:detail', post.pk)
    
def comments_create(request, post_id):
    #댓글을 달 게시물
    post = Post.objects.get(pk=post_id)
    #form에서 넘어온 댓글 내용
    content = request.POST.get('content')
    #댓글 생성 및 저장
    comment = Comment(post=post, content=content)
    comment.save()
    return redirect('posts:detail', post.pk)

def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('posts:detail', post_id)