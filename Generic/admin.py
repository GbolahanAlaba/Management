from django.contrib import admin
from .models import *
from .forms import *

class SIGNUP(admin.ModelAdmin):
    form = SignupForm 
    list_display = ['Fullname', 'Email', 'Empcode', 'Timestamp']
    list_filter = ['Fullname']
    search_fields = ['Fullname']

admin.site.register(Emp)
admin.site.register(Signup, SIGNUP)


# Register your models here.
