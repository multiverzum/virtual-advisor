from django.shortcuts import render
from django.shortcuts import render, redirect

def getHome(request):
    return render(request, 'home.html')
