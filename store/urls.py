from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('order/', views.order),
   
]
