from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.
def SignIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = auth.authenticate(
                request=request, username=username, password=password
            )

            if user is not None:
                auth.login(request, user)
                return redirect("home")

        return redirect("account:login")

    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

def SignUp(request):
    
    pass

def logout(request):
   auth.logout(request)
   return redirect('home')

