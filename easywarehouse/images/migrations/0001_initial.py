# Generated by Django 3.2 on 2021-05-30 15:32

from django.db import migrations, models
import django.db.models.deletion
import easywarehouse.storage_backends


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0009_auto_20210530_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(storage=easywarehouse.storage_backends.S3(), upload_to='')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
            options={
                'db_table': 'images',
            },
        ),
    ]