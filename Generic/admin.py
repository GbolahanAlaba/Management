from django.contrib import admin
from .models import *

# class SIGNUP(admin.ModelAdmin):
#     form = 
#     list_display = ['ID', 'Fullname', 'Email']
#     list_filter = ['Fullname']
#     search_fields = ['Fullname']

admin.site.register(Emp)
admin.site.register(Signup)


# Register your models here.
