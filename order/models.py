from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()

STATUSES = (
    ("verifying", "Verifying payment"),
    ("shipping", "Shipping"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),
)


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, default="verifying", max_length=100)
    paymentMethod = models.CharField(blank=True, max_length=100)
    price_paid = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}-{self.owner.username}"


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=STATUSES, default="verifying", max_length=100)

    class Meta:
        unique_together = [
            [
                "product",
                "order",
            ]
        ]

    def __str__(self):
        return f"{self.product.short_name}-{self.order.id}"


class OrderAddress(models.Model):
    name = models.CharField(blank=True, max_length=200)
    email_address = models.EmailField(blank=True, max_length=200)
    phone_number = models.CharField(blank=True, max_length=20)
    address = models.TextField(blank=True)
    zipcode = models.CharField(blank=True, max_length=50)
    city = models.CharField(blank=True, max_length=200)
    country = models.CharField(blank=True, max_length=200)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f"{self.name}-{self.order.id}"
