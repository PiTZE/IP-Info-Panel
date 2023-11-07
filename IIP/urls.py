from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_page, name="Home Page"),
    # path('instructions', ),
    path("status/", views.status_page, name="Server Status"),
]
