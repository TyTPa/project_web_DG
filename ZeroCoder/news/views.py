from django.shortcuts import render
from .models import News_post

def home(request):
	news = News_post.objects.all()
	return render(request, 'news/news.html',{'news': news})
# Create your views here.

def my_view(request):
# Проверяем, аутентифицирован ли пользователь
       if request.user.is_authenticated:
           username = request.user.username
       else:
           username = 'Гость'

       return render(request, 'my_template.html', {'username': username})