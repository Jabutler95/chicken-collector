from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chickens/', views.chicken_index, name='chicken-index'),
]