# Generated by Django 4.2.6 on 2023-11-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_cart_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='media'),
        ),
    ]
