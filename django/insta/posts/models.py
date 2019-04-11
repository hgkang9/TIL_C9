from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

#추가적인 저장 위치 만드는 함수
def post_image_path(instance, filename):
    return 'posts/{}/{}' .format(instance.content, filename)
    # return f'posts/images/{filename}' 권장
    # return f'posts/{instance.content}/{filename}' 가능 / filename은 확장자가 같이 들어있다
    # return f'posts/{instance.content}/{instance.content}.jpg' 파일명, 확장자 변경하면서 가능
    
class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #일대일로 가지고 있던 정보들을 없앨 때/cascade:1이 사라지면 N에 있던 가지고 있던 모든 정보 삭제
    content=models.TextField()
    # image=models.ImageField(blank=True) #빈 값이 들어갈 수 있도록 blank=True
    image=ProcessedImageField(
        # upload_to='posts/images', #저장위치
        upload_to=post_image_path,
        processors=[ResizeToFill(600,600)], #처리할 작업 목록
        format='JPEG', #저장포맷
        options={'quality':90}, #옵션
        )
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    
    #이미지 사용하고 싶을 때:pip install pillow
    #이미지 편집하고 싶을 때:pip install pilkit django-imagekit
    
class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #1대N 관계에서 1에 해당하는 것을 ()안에 써줌/user가 1,comment가 N
    post=models.ForeignKey(Post, on_delete=models.CASCADE) #//이중 1대N 관계
    content=models.TextField()
    