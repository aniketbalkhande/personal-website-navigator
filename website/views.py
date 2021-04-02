from website.models import Navigator
from django.shortcuts import render
from .models import Navigator

def home(request):
   return render(request,'home.html')

def navigator(request):
   websites = Navigator.objects.all()
   data = {
      'websites': websites
   }
   return render(request, 'website/navigator.html',data)

def login(request):
   return render(request, 'auths/login.html')

def signup(request):
   return render(request, 'auths/signup.html')







