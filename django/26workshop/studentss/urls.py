from django.urls import path
from . import views

app_name = 'studentss'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:student_id>/', views.detail, name='detail'),
]