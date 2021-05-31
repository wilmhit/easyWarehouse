from django.urls import path

from . import views

urlpatterns = [
    path("categories", views.ListCategories.as_view(), name="categories-list"),
    path("categories/add/", views.AddCategory.as_view(), name="categories-add"),
    path("categories/<int:pk>/update", views.UpdateCategory.as_view(), name="categories-update"),
    path(
        "categories/<int:pk>/details", views.CategoryDetails.as_view(), name="categories-details"
    ),
    path("categories/<int:pk>/delete/", views.DeleteCategory.as_view(), name="categories-delete"),
]
