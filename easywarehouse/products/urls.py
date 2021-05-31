from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("dashboard", views.dashboard),
    path("products", views.ListProducts.as_view(), name="products-list"),
    path("products/add/", views.AddProduct.as_view(), name="products-add"),
    path("products/<int:pk>/delete", views.DeleteProduct.as_view(), name="products-delete"),
    path("products/<int:pk>/details", views.ProductDetails.as_view(), name="products-details"),
    path("products/<int:pk>/update", views.UpdateProduct.as_view(), name="products-update"),
]
