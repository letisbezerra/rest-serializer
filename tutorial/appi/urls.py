from django.urls import path
from appi import views

urlpatterns = [
    path('appi/', views.appi_list),
    path('appi/<int:pk>/', views.appi_detail),
]