from django.shortcuts import render, redirect
from .models import CustomerInformations

# Create your views here.

def ilano_view(request):
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

	# return render(request, 'mainpage.html', {'CN':request.POST.get('Cusname'),
	# 	'AD':request.POST.get('CusAD'),
	# 	'CT':request.POST.get('Cusnum'),
	# 	'CX':request.POST.get('cusX'),
	# 	'CK':request.POST.get('chxX'),
	# 	})