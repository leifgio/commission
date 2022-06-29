from django.shortcuts import render, redirect
from .models import ClientInformations


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

      # return render(request, 'new_mainpage.html', {
      #    'newClientName':request.POST.get('Client'),
      #    'newClientphoneNo':request.POST.get('clientNo'),
      #    'newtimeSession':request.POST.get('SessTime')})''
