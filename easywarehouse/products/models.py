from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50)

class Products(models.Model):
    category = models.ForeignKey(Categories, models.DO_NOTHING)
    universal_id = models.UUIDField(unique=True)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    tags = models.TextField(blank=True, null=True)

class Images(models.Model):
    url = models.CharField(max_length=255)
    product = models.ForeignKey('Products', models.DO_NOTHING)