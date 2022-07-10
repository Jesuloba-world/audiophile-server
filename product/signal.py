from django.db.models.signals import post_save, post_delete
from .models import Product, MiniProduct


def create_update_mini_product(sender, instance, **kwargs):
    product = instance
    MiniProduct.objects.update_or_create(
        name=product.short_name,
        slug=product.slug,
        image=product.image
    )


def delete_mini_product(sender, instance, **kwargs):
    product = instance
    mini = MiniProduct.objects.get(name=product.short_name)
    mini.delete()


post_save.connect(create_update_mini_product, sender=Product)
post_delete.connect(delete_mini_product, sender=Product)
