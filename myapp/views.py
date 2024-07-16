from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def todo(request):
    return render(request,"todo.html")

def add_todo(request):
    return render(request,"add_todo.html")
