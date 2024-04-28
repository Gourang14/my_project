from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from myapp.models import contact
from datetime import datetime


=======
from django.http import response
import pickle
>>>>>>> 55cbde87b44a5a84dfc4c9cc5c7d0d229d5ea48a





# Create your views here.
def index(request):
<<<<<<< HEAD
  # if request.user.is_anonymous:
    #  return redirect("/login/")
=======
   #if request.user.is_anonymous:
      #return redirect("login/")
>>>>>>> 55cbde87b44a5a84dfc4c9cc5c7d0d229d5ea48a
   return render(request,'index.html')

def result(request):
   return render(request, "result.html")


def loginuser(request):
<<<<<<< HEAD
    if request.method == "POST":
        username = request.POST.get('username')  # Change to lowercase 'username'
        password = request.POST.get('password')  # Change to lowercase 'password'
=======
   
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
>>>>>>> 55cbde87b44a5a84dfc4c9cc5c7d0d229d5ea48a

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

<<<<<<< HEAD
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
=======
#views.py
from .forms import PredictionForm
from django.http import JsonResponse
import numpy as np

model_filepath = 'New_Task_Priority.pkl'

# Loading the model
print("Model filepath:", model_filepath)  # Print model filepath
try:
    with open(model_filepath, 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    print("Error loading model:", str(e))  # Print error message if loading fails

def TaskPre(request):
    form = PredictionForm(request.POST or None)
    prediction = None

    if request.method == 'POST' and form.is_valid():
        try:
            b_req = form.cleaned_data['B_Req']
            weights = form.cleaned_data['Weights']
            complexity = form.cleaned_data['Complexity']
            cost = form.cleaned_data['Cost']
            
            features = np.array([b_req, weights, complexity, cost]).reshape(1, -1)
            prediction = model.predict(features)[0]
        except Exception as e:
            print("Error during prediction:", str(e))  # Print error message if prediction fails

    context = {
        'form': form,
        'prediction': prediction
    }

    return render(request, 'TaskPre.html', context)
>>>>>>> 55cbde87b44a5a84dfc4c9cc5c7d0d229d5ea48a


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

 

  

  