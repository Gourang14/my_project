from django.contrib import admin
from django.urls import path,include
from myapp import views
from . import views



urlpatterns = [
   
    path('index.html',views.index,name ="index"),
    path('login',views.loginuser,name="login/"),
    path('logout',views.logoutuser,name="logout"),

    path('',views.index,name ="home"),
    path('result/',views.result, name = "result"),
    path('TaskPre/',views.TaskPre, name = "TaskPre")
    




    
]
