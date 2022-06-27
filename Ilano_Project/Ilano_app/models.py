from django.db import models

# Create your models here.
class CustomerInformations(models.Model):
	CustomerName = models.TextField(blank = True)
	CustomerContact = models.TextField(blank = True)
	CustomerAddress = models.TextField(blank = True)
	CustomerGender = models.TextField(blank = True)
	CustomerPackageType = models.TextField(blank = True)


class Customer(models.Model):
	Cus_Name = models.TextField(blank = True)
	Cus_Contact = models.TextField(blank = True)
	Cus_Address = models.TextField(blank = True)
	Cus_Email = models.TextField(blank = True)
	
	
class Order(models.Model):
	Cus_ID= models.ForeignKey(Customer,on_delete = models.CASCADE)
	Ord_Date = models.DateField()
	Ord_Price = models.TextField(blank = True)
	Ord_Detail = models.TextField(blank = True)
	Ord_Status = models.TextField(blank = True)

class Products(models.Model):
	Pro_Name = models.TextField(blank = True)
	Pro_Amount = models.TextField(blank = True)
	Pro_Price = models.TextField(blank = True)
	Pro_Detail = models.TextField(blank = True)


class Delivery(models.Model):
	Ord_ID = models.ForeignKey(Order,on_delete = models.CASCADE)
	Cus_ID = models.ForeignKey(Customer,on_delete = models.CASCADE)	
	Pro_ID = models.ForeignKey(Products,on_delete = models.CASCADE)
	Del_Detail = models.TextField(blank = True)
	Del_Price = models.TextField(blank = True)
	Del_Date = models.DateField()


class Review(models.Model):
	Cus_ID = models.ForeignKey(Customer,on_delete = models.CASCADE)	
	Pro_ID = models.ForeignKey(Products,on_delete = models.CASCADE)
	Rev_Comment = models.TextField(blank = True)
	Rev_Suggestion = models.TextField(blank = True)
