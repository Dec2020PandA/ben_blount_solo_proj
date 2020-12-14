from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('file/<int:id>', views.file),
    path('upload', views.upload_page),
    path('upload_file', views.upload),
    path('file/<int:id>/update', views.update),
    path('file/<int:id>/save', views.save)

    # path('file/<int:id>/edit', views.edit_file),
]
