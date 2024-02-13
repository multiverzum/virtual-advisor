from .views import getHome, getLogin, getRegister
from django.urls import path

urlpatterns = [

    path("", getHome, name='home'),
    path("login", getLogin, name='login'),
    path("register", getRegister, name='register'),

]