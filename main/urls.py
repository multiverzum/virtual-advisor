from .views import getHome, login_view, registerView, logout_view
from django.urls import path

urlpatterns = [

    path("", getHome, name='home'),
    path("login", login_view, name='login'),
    path("register", registerView, name='register'),
    path("logout", logout_view, name='logout'),

]