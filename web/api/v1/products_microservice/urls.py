from django.urls import path
from . import views

app_name = 'products_microservice'

urlpatterns = [
    path('hot-products/', views.HotProductsView.as_view(), name='hot-products')
]
