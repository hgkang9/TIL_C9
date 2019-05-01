from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required

def list(request):
    movies=Movie.objects.all()
    return render(request, 'list.html', {'movies':movies})

@login_required    
def create(request):
    movie_form=MovieForm()
    if request.method=="POST":
        movie_form=MovieForm(request.POST)
        if movie_form.is_valid():
            movie=movie_form.save(commit=False)
            movie.save()
            return redirect('movies:list')
    else:
        return render(request, 'forms.html', {'movie_form':movie_form})

def detail(request, movie_id):
    movie=get_object_or_404(Movie, id=movie_id)
    return render(request, 'detail.html', {'movie':movie})

@login_required    
def update(request, movie_id):
    movie=get_object_or_404(Movie, id=movie_id)
    if movie.user != request.user:
        return redirect('movies:list')
    if request.method=="POST":
        movie_form=MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie=movie_form.save(commit=False)
            movie.save()
            return redirect('movies:detail', movie_id)
    else:
        movie_form=MovieForm(instance=movie)
    return render(request, 'forms.html', {'movie_form':movie_form})

@login_required
def delete(request, movie_id):
    movie=get_object_or_404(Movie, id=movie_id)
    if movie.user != request.user:
        return redirect('movies:list')
    movie.delete()
    return redirect('movies:list')
    
@login_required
def like(request, movie_id):
    movie=get_object_or_404(Movie, id=movie_id)
    if request.user in movie.like_user.all():
        movie.like_user.remove(request.user)
    else:
        movie.like_user.add(request.user)
    return redirect('movies:detail', movie_id)