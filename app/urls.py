"""
Definition of urls for vehicleapis.
"""

from datetime import datetime
from django.urls import path
from . import views


urlpatterns = [
     path("upload_csv/",views.upload_csv, name="upload_csv"),     
]
