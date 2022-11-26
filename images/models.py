from django.db import models
import uuid


def product_directory_path(instance, filename):
    return f"product/{instance.alt_text}/{filename}"


def category_directory_path(instance, filename):
    return f"category/{instance.alt_text}/{filename}"


class ProductImage(models.Model):
    alt_text = models.CharField(max_length=100, null=True, blank=True)
    desktop = models.ImageField(
        upload_to=product_directory_path, verbose_name="Desktop Image"
    )
    tablet = models.ImageField(
        upload_to=product_directory_path, verbose_name="Tablet Image"
    )
    mobile = models.ImageField(
        upload_to=product_directory_path, verbose_name="Mobile Image"
    )

    def __str__(self):
        return self.alt_text


class CategoryImage(models.Model):
    alt_text = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to=category_directory_path)

    def __str__(self):
        return self.alt_text
