
from django.urls import path
from . import views

app_name = 'account'

url_patterns=[
    path("signin/", views.SignIn, name="Sign In"),
    path("signup/", views.SignUp, name="Sign Up")
]