from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


# Create your views here.
def new(request):
    form = StudentForm()
    return render(request, "new.html", {'form':form})
    
def create(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        age = form.cleaned_data.get('age')
        student = Student.objects.create(name=name, age=age)
        
    return redirect('studentss:detail', student.pk)
    
def detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'detail.html', {'student':student})
    