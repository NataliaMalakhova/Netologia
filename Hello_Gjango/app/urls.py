from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # домашняя страница
    path('current_time/', views.current_time_view, name='current_time'),  # текущее время
    path('workdir/', views.workdir_view, name='workdir'),  # содержимое рабочей директории
]
