from django.db import models
import uuid


def product_directory_path(instance, filename):
    return f"product/{instance.alt_text}/{filename}"


class ProductImage(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
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
