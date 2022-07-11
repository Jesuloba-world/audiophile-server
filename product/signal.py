from django.db.models.signals import post_save, post_delete
from .models import Product, MiniProduct
from django.core.exceptions import ObjectDoesNotExist


def create_update_mini_product(sender, instance, **kwargs):
    product = instance
    MiniProduct.objects.update_or_create(
        name=product.short_name,
        slug=product.slug,
        image=product.image
    )


def delete_mini_product(sender, instance, **kwargs):
    product = instance
    try:
        mini = MiniProduct.objects.get(name=product.short_name)
        mini.delete()
    except ObjectDoesNotExist:
        print("Didn't exist")


post_save.connect(create_update_mini_product, sender=Product)
post_delete.connect(delete_mini_product, sender=Product)
