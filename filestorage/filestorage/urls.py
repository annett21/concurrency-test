from django.contrib import admin
from django.urls import path
from static_files.views import get_dummy_static_file

urlpatterns = [
    path("admin/", admin.site.urls),
    path("static-dummy/<str:file_name>", get_dummy_static_file),
]
