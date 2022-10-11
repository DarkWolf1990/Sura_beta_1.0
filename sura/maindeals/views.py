from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def currentdeals(request):
    return render(request, 'maindeals/currentdeals.html')

def home(request):
    return render(request, 'maindeals/home.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'maindeals/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'maindeals/loginuser.html', {'form': AuthenticationForm(), 'error': "Username and "
                                                                                                       "password did "
                                                                                                       "not "
                                                                                                       " match"})
        else:
            login(request, user)
            return redirect('currentdeals')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


