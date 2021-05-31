from django.urls import path, include

from . import views

urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("products", include(products_urls)),
    path("images", include(images_urls)),
    path("categories", include(categories_urls)),
]
