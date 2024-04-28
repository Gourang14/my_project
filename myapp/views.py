from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import response
import pickle





# Create your views here.
def index(request):
   #if request.user.is_anonymous:
      #return redirect("login/")
   return render(request,'index.html')

def result(request):
   return render(request, "result.html")


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


   

    



