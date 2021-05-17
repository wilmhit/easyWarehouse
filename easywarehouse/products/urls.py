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
    path("categories", views.ListCategories.as_view(), name="categories-list"),
    path("categories/add/", views.AddCategory.as_view(), name="categories-add"),
    path("categories/<int:pk>/update", views.UpdateCategory.as_view(), name="categories-update"),
    path(
        "categories/<int:pk>/details", views.CategoryDetails.as_view(), name="categories-details"
    ),
    path("categories/<int:pk>/delete/", views.DeleteCategory.as_view(), name="categories-delete"),
    path("test", views.test),
    path("test_list", views.test_list),
]
