# Generated by Django 3.2 on 2022-07-11 01:25

from django.db import migrations, models
import images.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('alt_text', models.CharField(blank=True, max_length=100, null=True)),
                ('desktop', models.ImageField(upload_to=images.models.category_directory_path, verbose_name='Desktop Image')),
                ('tablet', models.ImageField(upload_to=images.models.category_directory_path, verbose_name='Tablet Image')),
                ('mobile', models.ImageField(upload_to=images.models.category_directory_path, verbose_name='Mobile Image')),
            ],
        ),
    ]