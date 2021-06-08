from uuid import uuid4

from categories.models import Category
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.base import ModelBase
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import reverse
from easywarehouse.settings import ELASTICSEARCH_HOST, ELASTICSEARCH_PORT, PRODUCTS_INDEX_NAME
from elasticsearch import Elasticsearch


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
        validators=[
            RegexValidator(regex="[0-9]+", message="The provided string is not a valid EAN.")
        ],
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Product(name={self.name})"

    def get_absolute_url(self):
        return reverse("products-details", kwargs={"pk": self.id})

    class Meta:
        db_table = "products"


@receiver(pre_delete, sender=Product, dispatch_uid="question_delete_signal")
def log_deleted_question(sender: ModelBase, instance: Product, using: str, **kwargs):
    Elasticsearch(hosts=[{"host": ELASTICSEARCH_HOST, "port": ELASTICSEARCH_PORT}]).delete(
        PRODUCTS_INDEX_NAME, instance.id
    )
    instance.save()
