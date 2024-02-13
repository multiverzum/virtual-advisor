from .views import getHome
from django.urls import path

urlpatterns = [

    path("", getHome, name='home'),

]