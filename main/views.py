from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task



def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    # Отправка данных методом POST для взаимодействия в базой данной django 
    if request.method == 'POST':
        # Данные заполненные от пользователя
        form = TaskForm(request.POST)
        # Проверка на корректность данных и сохранение их в БД
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверная'

    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create.html', context)