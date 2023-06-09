from django.db import models


class Emp(models.Model):
    Code = models.CharField(max_length=30)

    def __str__(self):
        return self.Code

class Signup(models.Model):
    Fullname = models.CharField(max_length=200, default='', blank=True, null=True)
    Empcode = models.CharField(max_length=100, default='', blank=True, null=True)
    Email = models.EmailField(max_length=180, default='', blank=True, null=True)
    Password = models.CharField(max_length=100, default='', blank=True, null=True)
    Timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.Fullname + ' ' + self.Email



# here
# Create your models here.
