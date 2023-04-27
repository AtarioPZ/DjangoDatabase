from django.contrib import admin
from django.urls import path
from dbase import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name='Home'),
    path("Home", views.home, name='home')
]