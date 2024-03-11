from django.shortcuts import render, HttpResponse
from .models import TodoItem, People
# Create your views here.

def home(request):
    return render(request, "GS/home.html", {})

def index(response):
    ls = People.objects.get(id=2)
    return render(response, "GS/list.html", {'names' : ls.names})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos: ": items})
