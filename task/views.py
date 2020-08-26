from django.shortcuts import render
from django.http import HttpResponse
from .models import *






def index(request):
    tasks = Tasks.object.all()

    context = {'tasks': tasks}
    return render(request,'list.html', context)
