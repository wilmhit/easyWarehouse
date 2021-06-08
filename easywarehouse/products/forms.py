from django.contrib.postgres.forms import SimpleArrayField
from django.forms import CharField, ModelForm

from . import models


class ProductForm(ModelForm):
    tags = SimpleArrayField(CharField(max_length=20))

    class Meta:
        model = models.Product
        fields = [
            "category",
            "name",
            "quantity",
            "good_availability_threshold",
            "ean",
            "tags",
            "description",
            "main_image_url",
        ]
