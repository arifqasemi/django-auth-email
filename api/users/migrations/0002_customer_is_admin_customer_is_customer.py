# Generated by Django 4.2.6 on 2023-11-19 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='is_customer',
            field=models.BooleanField(default=False),
        ),
    ]
