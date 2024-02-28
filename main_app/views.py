from django.shortcuts import render
from .models import Chicken

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def chicken_index(request):
  return render(request, 'chickens/index.html', { 'chickens': chickens })


