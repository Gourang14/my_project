from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login






# Create your views here.
def index(request):
   if request.user.is_anonymous:
      return redirect("/login/")
   return render(request,'index.html')

def loginuser(request):
   
   if request.method == "POST":
      username = request.POST.get('Username')
      passward = request.POST.get('Passward')
      print(Username,Passward)
      # CHECK IF HAS ENTERED CORRECT CREDENTIALS
      user = authenticate(Username = Username,Password=Password)
      if user is not None:
         login(request,user)
         return redirect("/")
      else:
         error_message = "Incorrect username or passward."
         return render(request,'login.html',{'error_message':error_message})

   return render(request,'login.html')

def logoutuser(request):
   logout(request)
   return redirect("/login")



   

    



