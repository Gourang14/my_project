from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout






# Create your views here.
def index(request):
   #if request.user.is_anonymous:
      #return redirect("login/")
   return render(request,'index.html')


def loginuser(request):
   
   if request.method == "POST":
      username = request.POST.get('Username')
      password = request.POST.get('Password')
      print(username,password)
      # CHECK IF HAS ENTERED CORRECT CREDENTIALS
      user = authenticate(Username = username,Password=password)
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



   

    



