from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView

from .forms import ImageForm
from .models import Image


class ImageDetails(LoginRequiredMixin, DetailView):
    template_name = "images/details.html"
    model = Image


class ListImages(LoginRequiredMixin, ListView):
    template_name = "images/list.html"
    model = Image
    queryset = Image.objects.all()


class DeleteImage(LoginRequiredMixin, DeleteView):
    template_name = "images/delete.html"
    model = Image
    success_url = reverse_lazy("images-list")


class AddImage(LoginRequiredMixin, CreateView):
    template_name = "images/add.html"
    form_class = ImageForm
    models = Image
