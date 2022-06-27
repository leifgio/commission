from django.db import models

# Create your models here.
class Info(models.Model):
	fullname = models.TextField (blank= True)
	sex= models.TextField (blank= True)
	age= models.TextField (blank= True)
	email= models.TextField (blank = True)
	height= models.TextField (blank= True)
	weight= models.TextField (blank= True)
	foodallergens= models.TextField (blank= True)

class Customer(models.Model):
	CusFName = models.TextField(blank = True)
	CusLName = models.TextField(blank = True)
	CusBlk = models.TextField(blank = True)
	CusBrgy = models.TextField(blank = True)
	CusMuni = models.TextField(blank = True)
	CusProv = models.TextField(blank = True)
	CusZip = models.TextField(blank = True)
	CusContactNo = models.TextField(blank = True)
	CusEmailAdd = models.TextField(blank = True)
	
class Order(models.Model):
	CusID = models.ForeignKey(Customer,on_delete = models.CASCADE)
	OrAmount = models.TextField(blank = True)
	OrDate = models.DateField()
	OrQty = models.TextField(blank = True)
	OrStatus = models.TextField(blank = True)

class Payment(models.Model):
	CusID= models.ForeignKey(Customer,on_delete = models.CASCADE)
	PayDate = models.DateField()
	PayType = models.TextField(blank = True)
	PayAmount = models.TextField(blank = True)

class Product(models.Model):
	ProdName = models.TextField(blank = True)
	ProdDesc = models.TextField(blank = True)
	ProdPrice = models.TextField(blank = True)
	ProdQty= models.TextField(blank = True)

class Delivery(models.Model):
	OrID = models.ForeignKey(Order,on_delete = models.CASCADE)
	CusID = models.ForeignKey(Customer,on_delete = models.CASCADE)	
	DeliveryType= models.TextField(blank = True)
	DeliveryDate = models.DateField()
	ArrivalDate = models.DateField()
