# Generated by Django 3.2 on 2023-02-14 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_order_price_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='grand_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderaddress',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]