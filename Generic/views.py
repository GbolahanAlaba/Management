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
        email = request.POST['email']
        password = request.POST['password']

        x = 'test@gmail.com'
        y = 'pass'

        if email != x and password != y:
            messages.info(request, 'Incorrect Email and Password')
            return render(request, 'signin.html')
        elif email != x:
            messages.info(request, 'Incorrect Email')
            return render(request, 'signin.html')
        elif password != y:
            messages.info(request, 'Incorrect Password')
            return render(request, 'signin.html')
        else:
            return redirect('homepage')

    return render(request, "signin.html")

# def createaccount(request):
#     return render(request, "create_account.html")