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

        def fun():
            Signup.objects.raw("delete * from Generic_emp where Code = 'CEO'")

        if login:
            fun()
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

def resetpassword(request):
    return render(request, 'reset-password.html')

def signup(request):

    if request.method == 'POST':
        fullname = request.POST['fullname']
        empcode = request.POST['emp']
        email = request.POST['email']
        password = request.POST['password']
        Repassword = request.POST['repassword']

        checkemp = Emp.objects.raw("select * from Generic_emp where Code = '%s'"%(empcode))
        checkemail = Signup.objects.raw("select * from Generic_signup where Email = '%s'"%(email))

        if password != Repassword:
            messages.info(request, 'Password not match')
            return render(request, 'signup.html')
        
        elif not checkemp:
            messages.info(request, 'Invalid Employement Code')
            return render(request, 'signup.html')
        
        elif checkemail:
            messages.info(request, 'Email exist')
            return render(request, 'signup.html')
        
        else:
            obj = Signup()
            obj.Fullname = fullname
            obj.Empcode = empcode
            obj.Email = email
            obj.Password = password
            obj.save()

            x = Signup.objects.raw("delete * from Generic_emp where Code = '%s'"%(empcode))
            return redirect("signin")

    return render(request, 'signup.html')
