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
        pwd = request.POST['password']

        login = Signup.objects.raw("select * from Generic_signup where Email = '%s' and Password = '%s'"%(email, pwd))
        email_exist = Signup.objects.raw("select * from Generic_signup where Email = '%s' and Password != '%s'"%(email, pwd))
        password_exist = Signup.objects.raw("select * from Generic_signup where Email != '%s' and Password = '%s'"%(email, pwd))

        # c = 'AJW-CSHR001'
        # csh = Signup.objects.raw("select * from Generic_signup where Empcode = '%s'"%(c))


        if login:
            return redirect('homepage')        
        
        elif email_exist:
            messages.info(request, 'Incorrect Password')
            return render(request, 'signin.html')
        
        elif password_exist:
            messages.info(request, 'Incorrect Email')
            return render(request, 'signin.html')
        
        else:
            messages.info(request, 'Incorrect Email and Password')
            return render(request, 'signin.html')

    return render(request, "signin.html")

# def createaccount(request):
#     return render(request, "create_account.html")