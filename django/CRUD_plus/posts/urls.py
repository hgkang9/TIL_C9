from django.urls import path
from . import views

urlpatterns = [
    path('naver/<str:q>/', views.naver), 
    path('github/<str:username>/', views.github),  #redirect는 페이지로 리턴하기 때문에 따로 html을 만들 필요가 없다
    path('', views.index, name='list'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
]
