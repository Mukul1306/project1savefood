from django.shortcuts import render,HttpResponse, redirect
from auth_app.models import Signupc, Donatec
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def Homef(request):
    return render(request,'auth\home.html')
from django.shortcuts import render
from django.http import HttpResponse
from .models import Signupc  # Assuming you have a model SignupC

def signupf(request):
    if request.method == "POST":
        username = request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        No = request.POST['No']

        if password != password_repeat:
            return render(request,"auth\signup 1.html")

        # Now save the user
        signup = Signupc(username=username,email=email, password=password, password_repeat=password_repeat,No=No)
        
        signup.save()

        return HttpResponse("Signup successful!")
    return render(request, 'auth\signup.html')
def aboutf(request):
    return render(request,'auth\sad.html')

def donatef(request):
    if request.method == "POST":
        namet = request.POST.get('name')
        location = request.POST.get('location')
        food = request.POST.get('food')
        hour = request.POST.get('hour')
        quantit = request.POST.get('quantit')
        donatef = Donatec(namet=namet,location=location, food=food, hour=hour,quantit=quantit)

        donatef.save()
        return render(request,"auth\home.html")

    return render(request, 'auth\donate.html')

def loginf(request):
    if request.method == "POST":
        first = request.POST['first']
        password3 = request.POST['password3']

        # Assuming Signupc is a model that holds the username and password
        try:
            user = Signupc.objects.get(username=first)  # Fetch user by username
            if user.password == password3:  # Check if password matches
                if user.No == 1:
                    return render(request,'auth\sngo.html')
                elif user.No == 2:
                    return render(request,'auth\donate.html')
                else:
                    return render(request,'auth\sell page.html')
                
            else:
                return render(request,'auth\login.html')
        except Signupc.DoesNotExist:
            return render(request,'auth\login.html')

    return render(request, 'auth\login.html')
@login_required
def sell_loginf(request):
    return render(request,'auth\sell login.html')
@login_required
def sell_pagef(request):
    return render(request,'auth\sell page.html')
@login_required
def helpf(request):
    return render(request,'auth\help.html')
@login_required
def ngof(request):
    return render(request,'auth\sngo.html')
def termf(request):
    return render(request,'auth\mterms.html')



 # mmmmmmmmmmmmmmmmmmmmmmmm