from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    Fullname = forms.CharField(required=True)
    Empcode = forms.CharField(required=True)
    Email = forms.CharField(required=True)
    password = forms.CharField(required=True)
   