from django.shortcuts import render, HttpResponse
from .models import TodoItem, People
# Create your views here.

def home(request):
    return render(request, "GS/home.html", {})

def index(response, id):
    ls = People.objects.get(id=id)
    return render(response, "GS/list.html", {"List" : ls})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos: ": items})
