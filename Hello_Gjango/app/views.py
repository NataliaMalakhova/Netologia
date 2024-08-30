from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import os

def home_view(request):
    # Список доступных страниц
    pages = {
        'Домашняя страница': '/',
        'Текущее время': '/current_time/',
        'Содержимое рабочей директории': '/workdir/'
    }
    # Используем render для рендеринга шаблона
    return render(request, 'app/home.html', {'pages': pages})

def current_time_view(request):
    # Получаем текущее время
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f"Текущее время: {current_time}")

def workdir_view(request):
    # Получаем список файлов и директорий в рабочей директории
    files = os.listdir('.')
    return HttpResponse(f"Содержимое рабочей директории: <br> {'<br>'.join(files)}")
