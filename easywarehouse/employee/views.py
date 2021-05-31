from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products.documents import ProductDocument
from products.models import Product


@login_required
def dashboard(req):
    return render(req, "employee/dashboard.html")
