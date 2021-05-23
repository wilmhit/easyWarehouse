from django.contrib.postgres.forms import SimpleArrayField
from django.forms import ModelForm, CharField

from . import models


class ProductForm(ModelForm):
    tags = SimpleArrayField(CharField(max_length=20))

    class Meta:
        model = models.Product
        fields = ["category", "name", "tags", "description"]


class CategoryForm(ModelForm):
    class Meta:
        model = models.Category
        fields = ["name"]


class ImageForm(ModelForm):
    class Meta:
        model = models.Image
        fields = ["image", "product"]
