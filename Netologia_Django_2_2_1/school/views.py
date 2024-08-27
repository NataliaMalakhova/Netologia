from django.shortcuts import render
from .models import Student

def students_list(request):
    students = Student.objects.prefetch_related('teachers').all()  # Использование prefetch_related для оптимизации
    return render(request, 'students_list.html', {'students': students})
