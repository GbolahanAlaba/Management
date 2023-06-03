from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Sum
# from .forms import *
from .models import *

# Create your views here.

def homepage(request):
    return render(request, "index.html")

def signin(request):
    return render(request, "signin.html")

# def createaccount(request):
#     return render(request, "create_account.html")