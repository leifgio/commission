from django.contrib import admin

from .models import Info, Customer, Product, Order, Payment, Delivery

admin.site.register(Info)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Delivery)
