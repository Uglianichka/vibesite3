from django.shortcuts import render
from django.http import HttpResponse
from  .models import Task

def index(request):
    task = Task.objects.all()
    return render(request, 'main/index.html', {'title':'Главная страница', 'tasks': task, 'image': 'img'})

def index_1(request):
    return render(request, template_name='main/home.html')

def about(request):
    return render(request, template_name='main/about.html')
