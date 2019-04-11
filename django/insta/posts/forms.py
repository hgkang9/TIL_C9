from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['content', 'image',] #어떤 데이터를 받을 건지 정의해주는 fields
        
class CommentForm(forms.ModelForm):
    content=forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'댓글을 작성하세요.'})) #추가적인 옵션 사용할 때:widget
    class Meta:
        model=Comment
        fields=['content',]