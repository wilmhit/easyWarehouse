# Generated by Django 3.2 on 2021-05-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_rename_max_quantity_product_good_availability_threshold"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="main_image_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
