from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name="list"),
    path('add/', views.add, name="add"),
    path('detail/<int:movie_id>/', views.detail, name="detail")
]