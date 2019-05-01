from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_id>/update/', views.update, name='update'),
    path('<int:movie_id>/delete/', views.delete, name='delete'),
    path('<int:movie_id>/like/', views.like, name='like'),
]