from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm,LoginForm
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request,'accounts/index.html')

def registration_view(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user-login")
    
    context = {"registration_form":form}
    return render(request,'accounts/registration.html',context=context)

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,username = username,password = password)
            if user is not None:    
                login(request,user)
                return redirect("dashboard")
        
    context = {'login_form':form}
    return render(request,'accounts/login.html',context=context)

def logout_view(request):
    logout(request)
    return redirect("")

@login_required(login_url='user-login')
def dashboard(request):
    return render(request,"accounts/dashboard.html")