from django.shortcuts import render, redirect
from .models import *
from .forms import CreateService, CreateArtist

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

def ArtistPage(request):
      artists = ArtistInformation.objects.all()
      context = {'artists':artists}
      return render(request,'artist.html',context)

def AddArtist(request):
    form = CreateArtist()
    if request.method == 'POST':
        artists = CreateArtist(request.POST)
        if artists.is_valid():
            artists.save()
            redirect('artist')
    value = {'form':form}
    artist_names = ArtistInformation.objects.all()
    return render(request,'addartist.html',value)

def AddService(request):
    form = CreateService()
    if request.method == 'POST':
        service = CreateService(request.POST)
        if service.is_valid():
            service.save()
    value = {'form':form}
    return render(request, 'addservice.html',value)
