from django.urls import path

from . import views

urlpatterns = [
    
    path('<int:receipt_id>/', views.receipt, name='receipt'),
    path('', views.receipts, name='receipts'),
]