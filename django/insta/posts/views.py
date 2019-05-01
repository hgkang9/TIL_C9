from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.views.decorators.http import require_POST, require_http_methods
from django.http import JsonResponse

def list(request):
    posts=Post.objects.order_by('-id').all() #정렬할 때 order_by/'-'붙이면 내림차순
    comment_form=CommentForm()
    return render(request, 'posts/list.html', {'posts':posts, 'comment_form':comment_form})

@login_required
def create(request):
    if request.method=='POST':
        post_form=PostForm(request.POST, request.FILES) #순서 중요
        if post_form.is_valid():
            post=post_form.save(commit=False)
            post.user=request.user
            post.save() #실제 DB에 저장
            return redirect('posts:list')
    else: #get요청일때
        post_form=PostForm()
    return render(request, 'posts/form.html', {'post_form':post_form})
    
@login_required
def update(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    if post.user!=request.user:
        return redirect('posts:list')
    if request.method=='POST':
        post_form=PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form=PostForm(instance=post) #수정하는 것이므로 위에서 가져온 정보들을 자동으로 폼에 바로 채워넣기 위해 사용(instance)
    return render(request, 'posts/form.html', {'post_form':post_form})
    
@login_required
def delete(request, post_id):
    # post=Post.objects.get(id=post_id) #pk=post_id도 가능
    post=get_object_or_404(Post, id=post_id)
    if post.user!=request.user:
        return redirect('posts:list')
    post.delete()
    # if post.user==request.user:
    #     post.delete()
    return redirect('posts:list')
    
@login_required
@require_POST #decorator는 순서에 영향 받음
def comment_create(request, post_id):
    comment_form=CommentForm(request.POST)
    if comment_form.is_valid():
        comment=comment_form.save(commit=False)
        comment.user=request.user
        comment.post_id=post_id
        comment.save()
    return redirect('posts:list')
    
@require_http_methods(['GET','POST'])    
def comment_delete(request, post_id, comment_id): #순서 중요
    comment=get_object_or_404(Comment, id=comment_id)
    if comment.user!=request.user:
        return redirect('posts:list')
    comment.delete()
    return redirect('posts:list')
    
def like(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    if request.user in post.like_users.all(): #all까지 해야 리스트 안에 있는지 검사 가능
        # 좋아요 취소
        post.like_users.remove(request.user)
        liked=False
    else:
        # 좋아요
        post.like_users.add(request.user)
        liked=True
    # return redirect('posts:list')
    return JsonResponse({'liked':liked, 'count':post.like_users.count()})
