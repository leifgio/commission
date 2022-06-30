from django.db import models

# Create your models here.
class ClientInformations(models.Model):
    last = models.TextField(blank = True)
    first = models.TextField(blank = True)
    email = models.TextField(blank = True)
    phone = models.TextField(blank = True)
    gender = models.TextField(blank = True)
    age = models.TextField(blank = True)
 
class ArtistInformation(models.Model):
    artistname = models.TextField(blank = True)

class Service(models.Model):
    SERVICE_TYPES = (
        ('T', 'Tattoo'),
        ('H', 'Henna'),
        ('P', 'Piercing'),
        )
    service_artist = models.TextField(blank = True)
    service_client = models.TextField(blank = True)
    service_date = models.DateField(blank = True)
    service_type = models.TextField(blank = True, choices=SERVICE_TYPES)

class Voucher(models.Model):
    VOUCHER_TYPES = (
        ('30', '30 percent'),
        ('40', '40 percent'),
        ('50', '50 percent'),
        )
    voucher_name = models.TextField(blank = True)
    voucher_type = models.TextField(blank = True, choices=VOUCHER_TYPES)
    voucher_date = models.TextField(blank = True)
    

class Payment(models.Model):
    PAYMENT_METHOD = (
        ('G', 'Gcash'),
        ('C', 'Cash'),
        ('P', 'Paymaya'),
        )
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    payment_voucher  = models.ForeignKey(Voucher, on_delete=models.CASCADE)

