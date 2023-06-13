from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signin/', views.signin, name='signin'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    path('signup/', views.signup, name='signup'),
    # path('newaccount/', views.createaccount, name='createaccount'),

]