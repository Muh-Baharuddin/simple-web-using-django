from turtle import title
from django.shortcuts import render, HttpResponse

# Create your views here.
def awal(request):
  return HttpResponse('berhasil diinstal')

def home(request):
  context={
    'title':title
  }
  return render(request, 'home.html', context)

def profile(request):
  context={
    'title':title
  }
  return render(request, 'profile.html', context)

def contact(request):
  context={
    'title':title
  }
  return render(request, 'contact.html', context)