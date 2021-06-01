from django.db import models
from django.urls import reverse
from products.models import Product

from easywarehouse.storage_backends import S3


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
