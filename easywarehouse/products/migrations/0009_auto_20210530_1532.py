# Generated by Django 3.2 on 2021-05-30 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_main_image_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='categories.Category'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
