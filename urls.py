from django.contrib import admin
from django.urls import path,include
from auth_app import views 

urlpatterns = [
    path('', views.Homef, name='Home page'),
    path('signup',views.signupf, name='signup'),
    path("about",views.aboutf,name='about'),
    path("donate",views.donatef,name='donate'),
    path("login",views.loginf,name='login'),
    path("selllogin",views.sell_loginf,name='sell login'),
    path("sellpage",views.sell_pagef,name='sell page'),
    path("help",views.helpf,name='help'),
    path('ngo', views.ngof, name='Ngos'),
    path('term', views.termf, name='Ngos'),


    # mmmmmmmmmmmmmmmmmmmmmmmm
]