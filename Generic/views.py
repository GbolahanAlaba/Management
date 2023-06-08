from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Sum
# from .forms import *
from .models import *

# Create your views here.

def homepage(request):
    return render(request, "index.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        x = 'gbolahan'
        y = 'pass'

        if username != x and password != y:
            messages.info(request, 'Invalid Login')
            return render(request, 'signin.html')
        elif username != x:
            messages.info(request, 'Incorrect Username')
            return render(request, 'signin.html')
        elif password != y:
            messages.info(request, 'Incorrect Password')
            return render(request, 'signin.html')
        else:
            return redirect('homepage')

    return render(request, "signin.html")

# def createaccount(request):
#     return render(request, "create_account.html")