from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(req):
    return render(req, "employee/dashboard.html")
