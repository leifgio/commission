from django.shortcuts import render, redirect
from .models import CustomerInformations, Review

# Create your views here.

def OrderPage(request):
	if request.method == "POST":
		CustomerInformations.objects.create(CustomerName=request.POST['Cusname'],
			CustomerContact=request.POST['Cusnum'],
			CustomerAddress=request.POST['CusAD'],
			CustomerGender=request.POST['cusXs'],
			CustomerPackageType=request.POST['chxX']
			)
		return redirect('/')
	CustomerInfoList = CustomerInformations.objects.all()
	return render(request, 'mainpage.html',{'registered_Customer_Info': CustomerInfoList})

def ReviewPage(request):
	if request.method == "POST":
		Review.objects.create(
			Cus_ID=request.POST['cusid'],
			Pro_ID=request.POST['proid'],
			Rev_Comment=request.POST['review'],
			Rev_Suggestion=request.POST['suggestion']
			)
		return redirect('/')
	review = Review.objects.all()
	return render(request, 'mainpage.html',{'review': review})

	Cus_ID = models.ForeignKey(Customer,on_delete = models.CASCADE)	
	Pro_ID = models.ForeignKey(Products,on_delete = models.CASCADE)
	Rev_Comment = models.TextField(blank = True)
	Rev_Suggestion = models.TextField(blank = True)
