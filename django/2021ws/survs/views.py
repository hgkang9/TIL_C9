from django.shortcuts import render
from .models import Question, Choice
# Create your views here.

def index(request):

    survs = Question.objects.all()
    
    return render(request, 'index.html', {'survs':survs})