from django.contrib import admin
from .models import Product, Category, Included, Image, Gallery

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Included)
admin.site.register(Image)
admin.site.register(Gallery)
