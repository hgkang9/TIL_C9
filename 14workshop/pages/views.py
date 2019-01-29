from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request, 'info.html')
    
def student(request, name):
    stu = {"홍길동":28, "김길동":27, "박길동":26}
    return render(request, 'student.html', {'name':name, 'age':stu[name]})
    
    
    
    # for i in stu:
    #     age = stu[i]
    # return render(request, 'student.html', {'name':age})
