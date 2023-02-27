from django.db import models
from product.models import Product


class Hero(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
    )
    copy = models.TextField(null=False, blank=True)
