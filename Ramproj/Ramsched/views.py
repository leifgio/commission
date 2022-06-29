from django.shortcuts import render, redirect
from .models import *

def MainPage(request):
      if request.method == "POST":
         ClientInformations.objects.create(
            last=request.POST['last'],
            first=request.POST['first'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            gender=request.POST['gender'],
            age=request.POST['age']
            )
         return redirect('/')
      client = ClientInformations.objects.all()
      return render(request,'new_mainpage.html',{'client':client})

def ServicePage(request):
      service = Service.objects.all()
      context = {'service':service}
      return render(request,'service.html',context)

def ArtistsPage(request):
      artist = ArtistInformation.objects.all()
      context = {'artist':artist}
      return render(request,'artist.html',context)

