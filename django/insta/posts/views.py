from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

def list(request):
    posts=Post.objects.all()
    return render(request, 'posts/list.html', {'posts':posts})

def create(request):
    if request.method=='POST':
        post_form=PostForm(request.POST, request.FILES) #순서 중요
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else: #get요청일때
        post_form=PostForm()
    return render(request, 'posts/create.html', {'post_form':post_form})
    
def update(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    if request.method=='POST':
        post_form=PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form=PostForm(instance=post) #수정하는 것이므로 위에서 가져온 정보들을 자동으로 폼에 바로 채워넣기 위해 사용(instance)
    return render(request, 'posts/create.html', {'post_form':post_form})
    
def delete(request, post_id):
    # post=Post.objects.get(id=post_id) #pk=post_id도 가능
    post=get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('posts:list')
    
