from django.forms import ModelForm

from . import models


class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        # TODO: Split the tags string during the serialization to save them as an array
        fields = ["category", "name", "tags"]


class CategoryForm(ModelForm):
    class Meta:
        model = models.Category
        fields = ["name"]
