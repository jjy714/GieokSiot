from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import TodoItem, People
from .forms import loginForm
# Create your views here.

def home(request):
    return render(request, "GS/home.html", {})

def index(response):
    ls = People.objects.get(id=2)
    return render(response, "GS/list.html", {'names' : ls.names})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "GS/todos.html", {"todos: ": items})

def login(response):
    if response.method == "POST":
        form = loginForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["ID"]
        return HttpResponseRedirect(f'/{n.id}')
    else:
        form = loginForm()
        
    return render(response, "GS/login.html", {"form": form}  )