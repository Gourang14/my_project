from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from myapp.models import contact
from datetime import datetime







# Create your views here.
def index(request):
  # if request.user.is_anonymous:
    #  return redirect("/login/")
   return render(request,'index.html')


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Change to lowercase 'username'
        password = request.POST.get('password')  # Change to lowercase 'password'

        user = authenticate(username=username, password=password)  # Correct function parameters
        if user is not None:
            login(request, user)
            return redirect("index")  # Redirect to 'index' view after successful login
        else:
            error_message = "Incorrect username or password."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def logoutuser(request):
   logout(request)
   return redirect("/login")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


def Contact(request):
  if request.method == "POST":
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')

    # Create a new Contact object
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email,
                          phone=phone, message=message, date=datetime.today())
    new_contact.save()

  return render(request, 'contact.html')

  def taskassigner(request):
 
   return render(request,'task.html')

 

  

  