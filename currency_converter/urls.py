from django.contrib import admin
from django.urls import path, include
from . import views

API_KEY = 'cur_live_XKf0Vm1furR8r1Q8WolbFzwqEzKv6bRrCuuaRvlO'  # убрать потом в переменные докера

urlpatterns = [
    path("convert_value/", views.convert_value),
]
