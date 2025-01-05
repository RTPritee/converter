from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("landing/", views.landing, name="landing"),
    path("file_upload/", views.file_upload, name="file_upload"),
    # path("convert/", views.convert_file),
    path("download/", views.download_csv, name="download_csv"),
     path("logout/", views.user_logout, name="logout"),  # Logout
]

