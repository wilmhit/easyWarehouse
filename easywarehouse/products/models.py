from uuid import uuid4

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Category(name={self.name})"

    def get_absolute_url(self):
        return reverse("categories-details", kwargs={"pk": self.id})

    class Meta:
        db_table = "categories"


class Product(models.Model):
    category = models.ManyToManyField(Category)
    public_id = models.UUIDField(unique=True, default=uuid4, db_index=True)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    tags = ArrayField(models.CharField(max_length=50), blank=True)

    def __str__(self):
        return f"Product(name={self.name})"

    def get_absolute_url(self):
        return reverse("products-details", kwargs={"pk": self.id})

    class Meta:
        db_table = "products"


class Image(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("images-details", kwargs={"pk": self.id})

    def __str__(self):
        return f"Image(url={self.image.url})"

    class Meta:
        db_table = "images"
