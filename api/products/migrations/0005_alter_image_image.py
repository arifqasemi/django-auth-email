# Generated by Django 4.2.6 on 2023-11-23 05:55

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to=products.models.upload_to),
        ),
    ]
