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
  chickens = Chicken.objects.all()
  return render(request, 'chickens/index.html', { 'chickens': chickens })

def chicken_detail(request, chicken_id):
  chicken = Chicken.objects.get(id=chicken_id)
  return render(request, 'chickens/detail.html', { 'chicken': chicken })
