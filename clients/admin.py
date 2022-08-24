from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Checkout)
admin.site.register(ChangePackage)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(ShiftingRequest)
admin.site.register(MpesaPayment)
