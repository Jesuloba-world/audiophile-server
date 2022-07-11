from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
import uuid
from images.models import ProductImage, product_directory_path, CategoryImage


class MiniProduct(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        unique=True,
    )
    slug = models.SlugField(null=True, unique=True, editable=True)
    image = models.OneToOneField(
        ProductImage, on_delete=models.SET_NULL, related_name="mini_images", null=True, blank=True
    )

    def __str__(self):
        return f"{self.name} mini"


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
    slug = models.SlugField(null=True, unique=True, editable=True)
    image = models.OneToOneField(
        CategoryImage, on_delete=models.SET_NULL, related_name="category_image", null=True, blank=True
    )

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
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="products",
    )
    image = models.OneToOneField(
        ProductImage, on_delete=models.SET_NULL, related_name="images", null=True, blank=True
    )
    slug = models.SlugField(null=True, unique=True, blank=True, editable=True)
    new = models.BooleanField(default=False)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=8)
    description = models.TextField(
        null=True,
        blank=True,
    )
    features = models.TextField(null=True, blank=True)
    others = models.ManyToManyField(
        MiniProduct,
        related_name="others",
        blank=True,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.short_name} {self.category.name}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Included(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    item = models.CharField(null=True, max_length=200)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="includes",
    )
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    class Meta:
        verbose_name = _("Include")
        verbose_name_plural = _("Includes")

    def __str__(self):
        return f"{self.quantity}x {self.item}"


class Gallery(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, blank=False, null=False
    )
    first = models.OneToOneField(
        ProductImage, on_delete=models.SET_NULL, null=True, blank=True, related_name="first"
    )
    second = models.OneToOneField(
        ProductImage, on_delete=models.SET_NULL, null=True, blank=True, related_name="second"
    )
    third = models.OneToOneField(
        ProductImage, on_delete=models.SET_NULL, null=True, blank=True, related_name="third"
    )

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")

    def __str__(self):
        return f"{self.product.short_name} gallery"
