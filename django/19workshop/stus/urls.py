from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new),
    path('create/', views.create),
    path('', views.index),
    path('<int:stu_id>/', views.detail),
    path('<int:stu_id>/delete/', views.delete),
    path('<int:stu_id>/edit/', views.edit),
    path('<int:stu_id>/update/', views.update),
]