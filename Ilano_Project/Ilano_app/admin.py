from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(CustomerInformations)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Products)
admin.site.register(Delivery)
admin.site.register(Review)



