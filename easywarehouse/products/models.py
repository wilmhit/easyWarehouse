from uuid import uuid4

from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

from easywarehouse.storage_backends import S3


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Category(name={self.name})"

    def get_absolute_url(self):
        return reverse("categories-details", kwargs={"pk": self.id})

    class Meta:
        db_table = "categories"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ManyToManyField(Category)
    public_id = models.UUIDField(unique=True, default=uuid4, db_index=True)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    good_availability_threshold = models.PositiveIntegerField()
    tags = ArrayField(models.CharField(max_length=50), blank=True)
    description = models.TextField(default="")
    main_image_url = models.URLField(null=True, blank=True)
    ean = models.CharField(
        max_length=13,
        validators=[RegexValidator(regex="[0-9]{13}", message="EAN can contain only numbers")],
        default="0000000000000",
    )

    def __str__(self):
        return f"Product(name={self.name})"

    def get_absolute_url(self):
        return reverse("products-details", kwargs={"pk": self.id})

    class Meta:
        db_table = "products"


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(storage=S3())
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, related_name="images"
    )

    def get_absolute_url(self):
        return reverse("images-details", kwargs={"pk": self.id})

    def __str__(self):
        return f"Image(url={self.image.url})"

    class Meta:
        db_table = "images"
