from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CategoryForm, ProductForm
from .models import Category, Product


# TODO: Move index and dashboard to another app
def index(request):
    return render(request, "index.html")

def test(request):
    return  render(request, "products/view.html")

def test_list(request):
    return render(request, "products/list.html")

@login_required
def dashboard(request):
    return HttpResponse("Hello employee. You are logged in")


class ListProducts(LoginRequiredMixin, ListView):
    template_name = "products/list.html"
    models = Product
    queryset = Product.objects.all()


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


# TODO: Move categories to separate app


class ListCategories(LoginRequiredMixin, ListView):
    template_name = "categories/list.html"
    models = Category
    queryset = Category.objects.all()


class CategoryDetails(LoginRequiredMixin, DetailView):
    template_name = "categories/details.html"
    model = Category


class AddCategory(LoginRequiredMixin, CreateView):
    template_name = "categories/add.html"
    form_class = CategoryForm
    success_url = reverse_lazy("categories-list")


class UpdateCategory(LoginRequiredMixin, UpdateView):
    template_name = "categories/update.html"
    form_class = CategoryForm
    success_url = reverse_lazy("categories-list")
    model = Category


class DeleteCategory(LoginRequiredMixin, DeleteView):
    template_name = "categories/delete.html"
    form_class = CategoryForm
    success_url = reverse_lazy("categories-list")
    model = Category
