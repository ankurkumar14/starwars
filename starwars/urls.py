
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [path(r"", include("favourite.urls")), path("admin/", admin.site.urls)]
