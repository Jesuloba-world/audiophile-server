from django.contrib import admin
from .models import Order, OrderProduct, OrderAddress

admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(OrderAddress)
