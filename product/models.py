from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
import uuid


class Category(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        unique=True,
    )
    slug = models.SlugField(null=True, unique=True, editable=False)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Product Name"),
        help_text=_("Required and unique"),
        unique=True,
    )
    short_name = models.CharField(max_length=15, blank=True, null=True, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    slug = models.SlugField(null=True, unique=True, blank=True, editable=False)
    new = models.BooleanField(default=False)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=8)
    description = models.TextField(
        null=True,
        blank=True,
    )
    features = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.short_name} {self.category.name}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
