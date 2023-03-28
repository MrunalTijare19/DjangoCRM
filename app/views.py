from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    messages.info(request, "Welcome to CRM")
    # Check to see logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate 
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You Have Been Logged Successfully")
            return redirect ('home')
        else:
            messages.warning(request, "There Was an Error. Please Try Again")
            return redirect ('home')
        
    return render(request,'home.html',{})


# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request,"You have Been Logged out....")
    return redirect ('home')

def register_user(request):
    return render(request,"register.html")

