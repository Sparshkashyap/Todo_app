from django.shortcuts import render,redirect

from .models import Todo
from datetime import datetime
# ==================================== Home vala page ==============================
def home(request):
    return render(request,'home.html')

# ==================================== todo page ===================================
def todo(request):
    result=Todo.objects.filter(is_complete=False)
    dic={
        "todos":result
    }
    return render(request,"todo.html",dic)

# =================================== add_todo page =================================
def add_todo(request):
    if request.method=="POST":
        user_task=request.POST.get("task")
        user_created_at=request.POST.get("created_at")
        
        new_todo=Todo(task=user_task,created_at=user_created_at)
        new_todo.save()
        
        return redirect("todo")
        
    return render(request,"add_todo.html")



# =================================== delete todo ==================================
def delete_todo(request,todo_id):
    
    todo=Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("todo")

# ==================================== update todo =================================

def update_todo(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    if request.method=="POST":
        user_task=request.POST.get("task")
        user_created_at=request.POST.get("created_at")
        
        todo.task=user_task
        todo.created_at=user_created_at
        todo.save()
        
        return redirect("todo")
    
    parameter={
        "todo":todo.task,
        "created_at":todo.created_at
    }
    
    return render(request,"update.html",parameter)
    
    
    
    
   
        
        
        
        
        
        
        
        
        
    todo=todo.objects.get(id=todo_id)
    todo.update()
    
    return render(request,"add_todo")

# ====================================== mark_completed todo =======================

def mark_complete(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.is_complete=True
    todo.save()   
    return redirect("todo")


# ======================================== proifile pic =============================

def profile_pic(request):
    return render(request,'profile_pic.html')   





