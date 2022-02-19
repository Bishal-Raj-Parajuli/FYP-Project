from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def LoginView(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'UserAuth/login.html')

def LoginProcess(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        login(request=request, user=user)
        return redirect("dashboard-view")
    else:
        messages.error(request, "Error in Login !! Invalid Details") 
        return redirect("login-view")

@login_required
def LogoutProcess(request):
    logout(request)
    messages.success(request, "Logout Sucessfully !!")
    return redirect("login-view")

@login_required
def DashboardView(request):
    return render(request, 'home.html')