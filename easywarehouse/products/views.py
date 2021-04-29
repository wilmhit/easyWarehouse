from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('<h1>Hello, this is index page</h1> <a href="/login">login</a>')
    return render(request, "../templates/index.html", content_type="text/html")


@login_required
def dashboard(request):
    return HttpResponse("Hello emoployee. You are logged in")
