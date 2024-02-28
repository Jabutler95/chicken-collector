from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Chicken: 
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

chickens = [
  Chicken('Ruth', 'Rhode Island Red', 'Truly a red chicken from Rhode Island.', 700),
  Chicken('Karen', 'Leghorn', 'Walks around very loudly.', 21),
  Chicken('Rizzle', 'Frizzle', 'For rizzle this Frizzle is named Rizzle.', 99),
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def chicken_index(request):
  return render(request, 'chickens/index.html', { 'chickens': chickens })
