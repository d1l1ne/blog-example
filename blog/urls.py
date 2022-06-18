from django.urls import path
from . import views


urlpatterns = [

path('', views.showblog, name='showblog'), #при открытии сайт/blog будет показываться страница, указанная в views.py уровня данного приложения
path('<int:post_id>/', views.post_details, name='post_details') #при открытии сайт/blog/айди_поста будет показываться страница конкретного поста

]