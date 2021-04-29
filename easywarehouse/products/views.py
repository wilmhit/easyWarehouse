from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


@login_required
def dashboard(request):
    return HttpResponse("Hello emoployee. You are logged in")
