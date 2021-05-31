from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListCategories.as_view(), name="categories-list"),
    path("add/", views.AddCategory.as_view(), name="categories-add"),
    path("<int:pk>/update", views.UpdateCategory.as_view(), name="categories-update"),
    path("<int:pk>/details", views.CategoryDetails.as_view(), name="categories-details"),
    path("<int:pk>/delete/", views.DeleteCategory.as_view(), name="categories-delete"),
]
