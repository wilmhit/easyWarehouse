import typing

from django.utils.functional import LazyObject
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


class PaginableDocumentSearchResults(LazyObject):
    def __init__(self, search_object):
        super().__init__()
        self._wrapped = search_object

    def __len__(self):
        return self._wrapped.count()

    def __getitem__(self, index: typing.Union[slice, str]):
        search_results = self._wrapped[index]
        if isinstance(index, slice):
            search_results = list(search_results)
        return search_results
