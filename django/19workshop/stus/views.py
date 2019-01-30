from django.shortcuts import render, redirect
from .models import Student

def new(request):
    return render(request, 'new.html')
    
def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    
    stu = Student(name=name, email=email, birthday=birthday, age=age)
    stu.save()
    
    return redirect(f'/stus/{stu.pk}/')
    
def index(request):
    
    stus = Student.objects.all()
    
    return render(request, 'index.html', {'stus':stus})
    
def detail(request, stu_id):
    stu = Student.objects.get(pk=stu_id)
    return render(request, 'detail.html', {'stu':stu})
    
def delete(request, stu_id):
    stu = Student.objects.get(pk=stu_id)
    stu.delete()
    return redirect('stus:list')
    
def edit(request, stu_id):
    stu = Student.objects.get(pk=stu_id)
    return render(request, 'edit.html', {'stu':stu})
    
def update(request, stu_id):
    stu = Student.objects.get(pk=stu_id)
    stu.name = request.POST.get('name')
    stu.email = request.POST.get('email')
    stu.birthday = request.POST.get('birthday')
    stu.age = request.POST.get('age')
    stu.save()
    return redirect(f'/stus/{stu_id}')