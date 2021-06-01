# Generated by Django 3.2 on 2021-06-01 08:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_ean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ean',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='EAN can contain only numbers', regex='[0-9]{13}')]),
        ),
    ]
