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

# Guest views


def index(request):
    return render(request, "index.html")


class ProductAvailabilityMixin:
    @staticmethod
    def get_ratio_json(product: Product) -> str:
        return json.dumps(
            {
                "id": str(product.public_id),
                "ratio": product.quantity / product.good_availability_threshold,
            }
        )


class GuestListProducts(ListView, ProductAvailabilityMixin):
    template_name = "products/list.html"
    models = Product

    def get_queryset(self, default_text_query: str = ""):
        query = self.request.GET.get("text-search", default_text_query)
        matched_products = ProductDocument.search().query(
            "simple_query_string", query=query, fields=["name^5", "description"]
        )
        return matched_products.to_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        products_with_ratios = [self.get_ratio_json(p) for p in context["object_list"]]
        context["products_with_ratios"] = products_with_ratios
        return context


class GuestProductDetails(DetailView, ProductAvailabilityMixin):
    template_name = "products_details.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_with_ratio"] = self.get_ratio_json(context["object"])
        return context

# Employee views

class ProductDetails(LoginRequiredMixin, GuestProductDetails):
    template_name = "employee/products/details.html"

class ListProducts(GuestListProducts):
    template_name = "employee/products/search.html"

    def get_queryset(self):
       return super().get_queryset(default_text_query="*")


class AddProduct(LoginRequiredMixin, CreateView):
    template_name = "employee/products/add.html"
    form_class = ProductForm
    success_url = reverse_lazy("products-list")


class UpdateProduct(LoginRequiredMixin, UpdateView):
    template_name = "employee/products/update.html"
    form_class = ProductForm
    success_url = reverse_lazy("products-list")
    model = Product


class DeleteProduct(LoginRequiredMixin, DeleteView):
    template_name = "employee/products/delete.html"
    success_url = reverse_lazy("products-list")
    model = Product
