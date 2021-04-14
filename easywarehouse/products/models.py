from django.contrib.postgres.fields import ArrayField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "categories"


class Product(models.Model):
    category = models.ManyToManyField(Category)
    public_id = models.UUIDField(unique=True)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    tags = ArrayField(models.CharField(max_length=50), blank=True)

    class Meta:
        db_table = "products"


class Image(models.Model):
    url = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "images"
