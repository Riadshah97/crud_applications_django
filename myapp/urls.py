
from django.urls import path
from . import views

urlpatterns = [
    # User endpoints
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserRetrivUpdaateDeleteView.as_view(), name='user-detail'),

    # Product endpoints
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDeleteView.as_view(), name='product-detail'),
]

