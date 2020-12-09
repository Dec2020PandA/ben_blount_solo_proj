from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('login_user/', views.login_user),
    path('logout/', views.logout),
    path('create_user/', views.create_user),
]
