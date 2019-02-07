from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('naver/<str:q>/', views.naver), 
    path('github/<str:username>/', views.github),  #redirect는 페이지로 리턴하기 때문에 따로 html을 만들 필요가 없다
    path('', views.index, name='list'),   #각각의 url관리를 위해 이름을 지어줌 / GET
    path('new/', views.new, name='new'),  # GET(new), POST(create)
    # path('create/', views.create, name='create'), 
    path('<int:post_id>/', views.detail, name='detail'), # GET
    path('<int:post_id>/delete/', views.delete, name='delete'), # GET(confirm), POST(delete)
    path('<int:post_id>/edit/', views.edit, name='edit'), # GET(edit), POST(update)
    # path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
]
