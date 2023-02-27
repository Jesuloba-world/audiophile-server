from django.db import models
from product.models import Product
from django.core.exceptions import ValidationError
from images.models import ProductImage


class Hero(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
    )
    copy = models.TextField(null=False, blank=True)
    image = models.OneToOneField(ProductImage, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.pk and Hero.objects.exists():
            raise ValidationError("There is can be only one Hero instance")
        return super(Hero, self).save(*args, **kwargs)

    def __str__(self):
        return "The hero section"
