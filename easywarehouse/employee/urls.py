from django.urls import path, include

from . import views

from products.urls import employee_urlpatterns as products_urls
from categories.urls import urlpatterns as categories_urls
from images.urls import urlpatterns as images_urls

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("products/", include(products_urls)),
    path("images/", include(images_urls)),
    path("categories/", include(categories_urls)),
]
