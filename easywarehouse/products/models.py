from uuid import uuid4

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from categories.models import Category


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

    def __str__(self):
        return f"Product(name={self.name})"

    def get_absolute_url(self):
        return reverse("products-details", kwargs={"pk": self.id})

    class Meta:
        db_table = "products"
