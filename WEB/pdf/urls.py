from django.contrib import admin
from django.urls import path

from . import views

app_name = "pdf"

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('addpdf/', views.addpdf, name = "addpdf"),
    path('pdf/<int:id>', views.detail, name = "detail"),
    path('update/<int:id>', views.updatepdf, name = "update"),
    path('delete/<int:id>', views.deletepdf, name = "delete"),
]