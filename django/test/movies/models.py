from django.db import models
from django.conf import settings

class Genre(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
        
class Movie(models.Model):
    title=models.CharField(max_length=30)
    audience=models.IntegerField()
    poster_url=models.TextField()
    description=models.TextField()
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_user=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movie")
    
class Score(models.Model):
    content=models.CharField(max_length=30)
    score=models.IntegerField()
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
