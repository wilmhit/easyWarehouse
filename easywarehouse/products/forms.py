from django.forms import ModelForm

from . import models


class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = ["category", "name", "tags"]  # TODO: Split tags to an array


class CategoryForm(ModelForm):
    class Meta:
        model = models.Category
        fields = ["name"]
