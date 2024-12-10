"""
Definition of urls for vehicleapis.
"""

from datetime import datetime
from django.urls import path,include
from django.contrib import admin
from app import forms, views


urlpatterns = [
    path('',include("app.urls")),
    path('admin/', admin.site.urls),
]
