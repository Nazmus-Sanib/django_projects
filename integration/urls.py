from django.urls import path
from .import views

urlpatterns = [
    path("", views.func, name = "index"),
    path("add/", views.add, name = "add"),
    path("add/addnum/", views.addnum, name = "addnum"),
    path("clear/", views.clear, name = "clear"),
    ]
