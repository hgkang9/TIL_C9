from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleModelForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid(): #조건들에 맞다면 true, 아니면 false 반환
            article = form.save()
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content) #밑 두 줄과 같은 역할
            # article = Article(title=title, content=content)
            # article.save()
            
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm()
        
    return render(request, 'form.html', {'form':form})
        
def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article':article})
    
def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleModelForm(instance=article)
        
    return render(request, 'form.html', {'form':form})