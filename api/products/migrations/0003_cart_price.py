# Generated by Django 4.2.6 on 2023-11-19 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_image_image_alter_image_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
