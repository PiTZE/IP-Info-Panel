from django.shortcuts import render
from .models import Server


def home_page(request):
    return render(request, "index.html")

def status_page(request):
    servers = Server.objects.all()
    return render(request, "status.html", {"servers": servers})
