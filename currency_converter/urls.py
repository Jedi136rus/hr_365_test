from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("rates", views.convert_value),
]
