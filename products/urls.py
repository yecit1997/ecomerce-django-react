from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_products),
    path('get/<str:name>/', views.get_product),
    path('post/', views.create_produc),
    path('edit/<int:pk>/', views.edit_produc),
    path('delete/<int:pk>/', views.delete_produc),
    
]
