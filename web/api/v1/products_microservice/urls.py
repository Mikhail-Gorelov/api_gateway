from django.urls import path
from . import views

app_name = 'products_microservice'

urlpatterns = [
    path('hot-products/', views.HotProductsView.as_view(), name='hot-products'),
    path('secure/', views.SecureView.as_view()),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('product/', views.ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]
