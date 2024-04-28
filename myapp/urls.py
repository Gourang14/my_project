from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.views.generic import RedirectView






urlpatterns = [
     # Redirect the empty path to the login page
    path('', RedirectView.as_view(url='/login', permanent=False)),
    # Include admin URLs
    path('admin/', admin.site.urls), 
    path('index.html',views.index,name ="index"),
    path('login',views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"), 
    #contact path
    path('contact', views.contact, name="contact"),
    path('task', views.task, name="task"),
    
]
