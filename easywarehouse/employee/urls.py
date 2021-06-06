from categories.urls import urlpatterns as categories_urls
from django.urls import include, path
from images.urls import urlpatterns as images_urls
from products.urls import employee_urlpatterns as employee_products_urls

from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("products/", include(employee_products_urls)),
    path("images", include(images_urls)),
    path("categories/", include(categories_urls)),
]
