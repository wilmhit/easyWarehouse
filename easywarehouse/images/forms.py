from django.forms import ModelForm

from . import models


class ImageForm(ModelForm):
    class Meta:
        model = models.Image
        fields = ["image", "product"]
