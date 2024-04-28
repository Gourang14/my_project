from django.contrib import admin
from django.urls import path,include
from myapp import views
<<<<<<< HEAD
from django.views.generic import RedirectView



=======
from . import views
>>>>>>> 55cbde87b44a5a84dfc4c9cc5c7d0d229d5ea48a



urlpatterns = [
     # Redirect the empty path to the login page
    path('', RedirectView.as_view(url='/login', permanent=False)),
    # Include admin URLs
    path('admin/', admin.site.urls), 
    path('index.html',views.index,name ="index"),
<<<<<<< HEAD
    path('login',views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"), 
    #contact path
    path('contact', views.contact, name="contact"),
    path('task', views.task, name="task"),
=======
    path('login',views.loginuser,name="login/"),
    path('logout',views.logoutuser,name="logout"),

    path('',views.index,name ="home"),
    path('result/',views.result, name = "result"),
    path('TaskPre/',views.TaskPre, name = "TaskPre")
    




>>>>>>> 55cbde87b44a5a84dfc4c9cc5c7d0d229d5ea48a
    
]
