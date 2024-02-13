from django.shortcuts import render
from django.shortcuts import render, redirect

def getHome(request):
    return render(request, 'home.html')

def getLogin(request):
    return render(request, 'login.html')

def getRegister(request):
    return render(request, 'register.html')
