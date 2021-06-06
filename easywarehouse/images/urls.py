from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListImages.as_view(), name="images-list"),
    path("/add", views.AddImage.as_view(), name="images-add"),
    path("/<int:pk>/delete", views.DeleteImage.as_view(), name="images-delete"),
    path("/<int:pk>/details", views.ImageDetails.as_view(), name="images-details"),
]
