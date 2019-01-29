from django.urls import path
from . import views

urlpatterns = [
    path('naver/<str:q>/', views.naver), 
    path('github/<str:username>/', views.github),  #redirect는 페이지로 리턴하기 때문에 따로 html을 만들 필요가 없다
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:post_id>/', views.detail),
    path('<int:post_id>/delete/', views.delete),
    path('<int:post_id>/edit/', views.edit),
    path('<int:post_id>/update/', views.update),
]
