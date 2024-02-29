from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chickens/', views.chicken_index, name='chicken-index'),
  path('chickens/<int:chicken_id>/', views.chicken_detail, name='chicken-detail'),
  path('chickens/create/', views.ChickenCreate.as_view(), name='chicken-create'),
  path('chickens/<int:pk>/update/', views.ChickenUpdate.as_view(), name='chicken-update'),
  path('chickens/<int:pk>/delete/', views.ChickenDelete.as_view(), name='chicken-delete'),
  path('chickens/<int:chicken_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
]