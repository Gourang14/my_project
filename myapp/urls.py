from django.contrib import admin
from django.urls import path,include
from myapp import views



urlpatterns = [
   
    path('index.html',views.index,name ="index"),
    path('login',views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"),


    




    
]
