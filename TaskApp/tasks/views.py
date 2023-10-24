from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {'tasks': tasks})

#Add a new Task
def add(request):
    return render(request, 'tasks/add.html')
