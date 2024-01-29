
from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('animals', views.animals),
    path('add_animal',views.add_animal),
    path('login/', views.MyTokenObtainPairView.as_view())
]
