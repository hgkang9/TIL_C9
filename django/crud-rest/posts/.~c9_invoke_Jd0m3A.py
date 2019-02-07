from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) #최대길이 필수적으로 정해줘야 한다
    content = models.TextField()
    
    def __str__(self):
        return self.title
        
        
class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
# Post : Comment = 1 : N(ForeignKey)
# on_delete 옵션
# 1. CASCADE : 부모가 삭제되면, 자기 자신도 삭제
# 2. PROTECT : 자식이 존재하면, 부모 삭제 불가능
# 3. SET_NULL : 부모가 삭제되면, 자식의 부모 정보에 NULL 설정
    
    
# 1. Create
# post = Post(title='hello', content='world')
# post.save() 실제 데이터베이스에 저장

# 2. Read (저장된 내용 가져오는 방법)
# 2.1. All
# posts = Post.objects.all() 데이터베이스에 있는 자료 확인할 때/리스트로 가져오기 때문에 posts/반복가능
# 2.2. Get one
# post = Post.objects.get(pk=1) 자료 하나/반복불가능/장고는 일반적으로 pk를 쓴다
# 2.3. filter (WHERE)
# posts = Post.objects.filter(title='Hello').all()
# post = Post.objects.filter(title='Hello').first()
# 2.4. LIKE
# posts = Post.objects.filter(title__contains='He').all()
# 2.5. order_by(정렬)
# posts = Post.objects.order_by('title').all() 오름차순
# posts = Post.objects.order_by('-title').all() 내림차순
# 2.6. limit & offset
# [offset:offset+limit]
# posts = Post.objects.all()[1:2]

# 3. Delete
# post = Post.objects.get(pk=2)
# post.delete()

# 4. Update
# post = Post.objects.get(pk=1)
# post.title = 'hi'
# post.save()