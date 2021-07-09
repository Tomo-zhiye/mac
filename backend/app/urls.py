from django.urls import path
from app import views


urlpatterns = [
    path('property/', views.PropertyView.as_view(), name='property'),
    path('property/<str:pk>/', views.PropertyDetailView.as_view(), name='property-detail'),
]