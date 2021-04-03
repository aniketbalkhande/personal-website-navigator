from website.models import Navigator
from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from .models import Navigator

def home(request):
   return render(request,'home.html')

def navigator(request):
   websites = Navigator.objects.all()
   data = {
      'websites': websites
   }  
   if request.method == 'POST':
      website = request.POST['website']
      url = request.POST['url'] 

      navigator = Navigator(website = website, url = url)
      navigator.save()
      messages.success(request, 'New Website Bookmarked')
      return redirect('website:navigator')

   return render(request, 'website/navigator.html',data)

def deleteWebsite(request,id):
   website_to_delete = Navigator.objects.get(id=id)
   website_to_delete.delete()
   return HttpResponseRedirect('/site')








