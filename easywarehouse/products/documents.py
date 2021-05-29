from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import Product


@registry.register_document
class ProductDocument(Document):
    class Index:
        name = "products"

    class Django:
        model = Product
        # TODO: Add tags - not working out of the box
        fields = ("id", "name", "description", "main_image_url")
        ignore_signals = True
