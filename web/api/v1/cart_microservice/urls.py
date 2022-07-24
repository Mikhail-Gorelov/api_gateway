from django.urls import path
from . import views

app_name = 'cart_microservice'

urlpatterns = [
    path('cart/add/', views.CartAddView.as_view(), name='cart-add'),
    path('item/add/', views.ItemAddView.as_view(), name='item-add'),
]
