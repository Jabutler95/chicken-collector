from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chicken, Toy
from .forms import FeedingForm
from django.contrib.auth.views import LoginView




# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def chicken_index(request):
  chickens = Chicken.objects.filter(user=request.user)
  return render(request, 'chickens/index.html', { 'chickens': chickens })

@login_required
def chicken_detail(request, chicken_id):
  chicken = Chicken.objects.get(id=chicken_id)
  toys_chicken_doesnt_have = Toy.objects.exclude(id__in = chicken.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'chickens/detail.html', { 'chicken': chicken,
  'feeding_form': feeding_form, 'toys': toys_chicken_doesnt_have })

@login_required
def add_feeding(request, chicken_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.chicken_id = chicken_id
    new_feeding.save()
  return redirect('chicken-detail', chicken_id=chicken_id)

class ChickenCreate(LoginRequiredMixin, CreateView):
  model = Chicken
  fields = ['name', 'breed', 'description', 'age']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ChickenUpdate(LoginRequiredMixin, UpdateView):
  model = Chicken 
  fields = ['breed', 'description', 'age']

class ChickenDelete(LoginRequiredMixin, DeleteView):
  model = Chicken
  success_url = '/chickens/'

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, chicken_id, toy_id):
  Chicken.objects.get(id=chicken_id).toys.add(toy_id)
  return redirect('chicken-detail', chicken_id=chicken_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('chicken-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
