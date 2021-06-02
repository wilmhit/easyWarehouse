from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.GuestListProducts.as_view(), name="search"),
    path("products/<int:pk>", views.GuestProductDetails.as_view(), name="products-guest"),
]

employee_urlpatterns = [
    path("", views.ListProducts.as_view(), name="products-list"),
    path("add/", views.AddProduct.as_view(), name="products-add"),
    path("<int:pk>/delete", views.DeleteProduct.as_view(), name="products-delete"),
    path("<int:pk>/details", views.ProductDetails.as_view(), name="products-details"),
    path("<int:pk>/update", views.UpdateProduct.as_view(), name="products-update"),
]
