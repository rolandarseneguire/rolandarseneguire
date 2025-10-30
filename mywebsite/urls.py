from django.contrib import admin
from django.urls import path
from mywebsite import views
urlpatterns =[
    path('index/',views.index,name="index"),
    path('',views.home,name="home"),
]
