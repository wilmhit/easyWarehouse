import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .documents import ProductDocument
from .forms import ProductForm
from .models import Product


def index(request):
    return render(request, "index.html")


@login_required
def dashboard(request):
    return HttpResponse("Hello employee. You are logged in")


# Products


class ProductAvailabilityMixin:
    @staticmethod
    def _get_ratio_json(product: Product) -> str:
        return json.dumps(
            {
                "id": str(product.public_id),
                "ratio": product.quantity / product.good_availability_threshold,
            }
        )


class ListProducts(LoginRequiredMixin, ListView, ProductAvailabilityMixin):
    template_name = "products/list.html"
    models = Product
    queryset = Product.objects.all()

    def get_queryset(self):
        query = self.request.GET.get("text-search", "")
        matched_products = ProductDocument.search().query(
            "simple_query_string", query=query, fields=["name^5", "description"]
        )
        return matched_products.to_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        products_with_ratios = [self._get_ratio_json(p) for p in context["object_list"]]
        context["products_with_ratios"] = products_with_ratios
        return context


class ProductDetails(LoginRequiredMixin, DetailView, ProductAvailabilityMixin):
    template_name = "products/details.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_with_ratio"] = self._get_ratio_json(context["object"])
        return context


class AddProduct(LoginRequiredMixin, CreateView):
    template_name = "products/add.html"
    form_class = ProductForm
    success_url = reverse_lazy("products-list")


class UpdateProduct(LoginRequiredMixin, UpdateView):
    template_name = "products/update.html"
    form_class = ProductForm
    success_url = reverse_lazy("products-list")
    model = Product


class DeleteProduct(LoginRequiredMixin, DeleteView):
    template_name = "products/delete.html"
    success_url = reverse_lazy("products-list")
    model = Product
