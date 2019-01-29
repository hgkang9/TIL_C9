from django.db import models

# Create your models here.
class Student(models.Model): #모델의 이름은 테이블의 이름
    name = models.CharField(max_length=100) #최대길이 필수적으로 정해줘야 한다
    email = models.CharField(max_length=100)
    birthday = models.DateField()
    age = models.IntegerField()
    
    def __str__(self):
        return self.name