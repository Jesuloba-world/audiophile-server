# Generated by Django 3.2 on 2022-07-14 10:25

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20220711_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryimage',
            name='image',
            field=models.ImageField(upload_to=images.models.category_directory_path),
        ),
    ]
