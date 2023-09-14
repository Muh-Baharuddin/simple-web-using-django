from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
  path('', views.awal, name='awal'),
  path('home', views.home, name='home'),
  path('profile', views.profile, name='profile'),
  path('contact', views.contact, name='contact'),
]
