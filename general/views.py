from django.shortcuts import render
from django.http import HttpRequest



def welcome(request: HttpRequest):
    return render(request, "welcome.html")
