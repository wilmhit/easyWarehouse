from django.urls import path

from . import views

urlpatterns = [
    path("images", views.ListImages.as_view(), name="images-list"),
    path("images/add", views.AddImage.as_view(), name="images-add"),
    path("images/<int:pk>/delete", views.DeleteImage.as_view(), name="images-delete"),
    path("images/<int:pk>/details", views.ImageDetails.as_view(), name="images-details"),
]
