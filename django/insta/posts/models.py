from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    content=models.TextField()
    # image=models.ImageField(blank=True) #빈 값이 들어갈 수 있도록 blank=True
    image=ProcessedImageField(
        upload_to='posts/images', #저장위치
        processors=[ResizeToFill(600,600)], #처리할 작업 목록
        format='JPEG', #저장포맷
        options={'quality':90}, #옵션
        )
    
    #이미지 사용하고 싶을 때:pip install pillow
    #이미지 편집하고 싶을 때:pip install pilkit django-imagekit