from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.

# 初期Index
"""
def index(request):
    return HttpResponse("Hello, world!")
"""
    
def index(request):
    return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

# 初期バージョンの　Great
""" 
def greet(request, name):
    return HttpResponse(f"Hello, {name}!")
"""

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def index(request):
    return render(request, "hello/index.html")