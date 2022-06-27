from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Info 


def  MainPage(request):

	if request.method == "POST":
		Info.objects.create(fullname=request.POST['fname'], 
			sex=request.POST['genders'], 
			age=request.POST['age1'],
			email=request.POST['EAdd'],
			height=request.POST['EHeight'],
			weight=request.POST['EWeight'],
			foodallergens=request.POST['Allergen1'])
		return redirect('/')
	InfoList = Info.objects.all()
	return render(request, 'mainpage.html',{'registered_Info':InfoList})


	#request.method == 'POST':
		#return HttpResponse (request.POST['name'])
	#return render(request, 'mainpage.html' , {
	#	'NewName':request.POST.get('name'), 
	#	'NewE_Add':request.POST.get('E_Add'), 
	#	'NewEMessage':request.POST.get('EMessage'), 
	#	'NewFName':request.POST.get('fname'), 
	#	'NewRB':request.POST.get('gender2'), 
	#	'NewAge':request.POST.get('age1'), 
	#	'NewEAdd':request.POST.get('EAdd'), 
	#	'NewEHeight':request.POST.get('EHeight'), 
	#	'NewEWeight':request.POST.get('EWeight'), 
	#	'NewAllergen6':request.POST.get('Allergen6'),
	#	'NewAllergen10':request.POST.get('Allergen10'),
	#	'NewAllergen13':request.POST.get('Allergen13'),


		
