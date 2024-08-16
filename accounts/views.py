from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    
    if request.method=="POST":
    
        input_username=request.POST.get("username")
        input_password=request.POST.get("password")
        
        # print( input_username, input_password)
        
        user=auth.authenticate(username=input_username , password=input_password)
        # print(user)
        
        if user is not None:
            auth.login(request,user) # session create karna ka liye
            return redirect("todo")
        else:
            return redirect("home")
  
        
    return render(request,"accounts/login.html")


def register(request):
    
    if request.method=='POST':
        input_username=request.POST.get("username")
        input_password=request.POST.get("password")
        # first_name=request.POST.get("firstname")
        # lst_name=request.POST.get("lst_name")
        # user_email=request.POST.get("email")
    
    # if User.objects.filter(input_username=input_username).exists():
    #     messages.error(request, "Username already exists.")
    #     return redirect('register')
    
    
        
        newuser=User(username=input_username)
            # Firstname=first_name,
            # Lastname=lst_name,
            # Emailaddress=user_email)
       
        newuser.set_password(input_password)
        newuser.save()
        
      
        return redirect('login')
    
    return render(request,"accounts/register.html")





























