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


class ListProducts(LoginRequiredMixin, ListView):
    template_name = "products/list.html"
    models = Product
    queryset = Product.objects.all()

    def get_queryset(self):
        query = self.request.GET.get("text-search", "")
        matched_products = ProductDocument.search().query(
            "simple_query_string", query=query, fields=["name^5", "description"]
        )
        return matched_products


class ProductDetails(LoginRequiredMixin, DetailView):
    template_name = "products/details.html"
    model = Product


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
