from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("convert/", views.convert_file),
]
