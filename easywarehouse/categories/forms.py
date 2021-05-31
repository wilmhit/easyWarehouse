from django.forms import ModelForm

from . import models


class CategoryForm(ModelForm):
    class Meta:
        model = models.Category
        fields = ["name"]
