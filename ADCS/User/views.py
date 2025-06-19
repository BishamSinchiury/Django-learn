from django.shortcuts import render
from .models import Task
from django.http import HttpResponse

# Create your views here.
def home(request):
    data = [
        {'id': 1, 'title': 'Task 1'},
        {'id': 2, 'title': 'Task 2'},
        {'id': 3, 'title': 'Task 3'},
    ]
    return render(request, 'website/index.html', context={"tasks": data})