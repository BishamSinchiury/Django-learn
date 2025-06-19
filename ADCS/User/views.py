from django.shortcuts import render
from .models import Task
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'website/index.html')