from django.urls import path
from . import views

app_name = "survs"

urlpatterns = [
    path('', views.index, name='list'),
]