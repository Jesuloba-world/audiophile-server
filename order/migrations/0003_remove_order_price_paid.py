# Generated by Django 3.2 on 2023-02-03 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20230203_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price_paid',
        ),
    ]
