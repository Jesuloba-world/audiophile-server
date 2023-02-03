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
    status = models.CharField(choices=STATUSES, default="verifying")
    paymentMethod = models.CharField(blank=True)
    price_paid = models.DecimalField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}-{self.owner.username}"


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=STATUSES, default="verifying")

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
    name = models.CharField(blank=True)
    email_address = models.EmailField(blank=True)
    phone_number = models.CharField(blank=True)
    address = models.CharField(blank=True)
    zipcode = models.CharField(blank=True)
    city = models.CharField(blank=True)
    country = models.CharField(blank=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f"{self.name}-{self.order.id}"
