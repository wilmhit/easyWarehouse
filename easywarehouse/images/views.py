from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView

from .forms import ImageForm
from .models import Image


class ImageDetails(LoginRequiredMixin, DetailView):
    template_name = "employee/images/details.html"
    model = Image


class ListImages(LoginRequiredMixin, ListView):
    template_name = "employee/images/list.html"
    model = Image
    queryset = Image.objects.all()


class DeleteImage(LoginRequiredMixin, DeleteView):
    template_name = "employee/images/delete.html"
    model = Image
    success_url = reverse_lazy("images-list")


class AddImage(LoginRequiredMixin, CreateView):
    template_name = "employee/images/add.html"
    form_class = ImageForm
    models = Image
