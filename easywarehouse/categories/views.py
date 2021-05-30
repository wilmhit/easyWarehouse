from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CategoryForm
from .models import Category

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
