from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method=="POST":
        signup_form=UserCreationForm(request.POST)
        if signup_form.is_valid():
            user=signup_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        signup_form=UserCreationForm()
    return render(request, 'signup.html', {'signup_form':signup_form})
    
def login(request):
    if request.method=="POST":
        login_form=AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        login_form=AuthenticationForm()
    return render(request, 'login.html', {'login_form':login_form})
    
def logout(request):
    auth_logout(request)
    return redirect('movies:list')