from django.db import models
import uuid
from product.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class CartItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [
            [
                "product",
                "owner",
            ]
        ]

    def __str__(self):
        return f"{self.product.short_name}-{self.owner.username}"
