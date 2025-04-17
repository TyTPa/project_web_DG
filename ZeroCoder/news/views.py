from django.shortcuts import render,redirect
from .models import News_post
from .forms import News_postForm

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

def create_news(request):
        error=''
        if request.method == 'POST':
            form = News_postForm(request.POST)            # Сюда сохранится информация от пользователя.

            if form.is_valid():
                news_post = form.save(commit=False)
                news_post.user = request.user.username  # Установите автора текущим пользователем
                news_post.save()
                return redirect ('news_home')

            else:
                error = "Данные были заполнены некорректно"

        form = News_postForm()
        return render(request, 'news/add_new_post.html', {'form': form, 'error': error})

