from django.urls import path
from . import views

app_name = 'cart_microservice'

urlpatterns = [
    path('cart/add/', views.CartAddView.as_view(), name='cart-add'),
    path('item/add/', views.ItemAddView.as_view(), name='item-add'),
    path('cart/show/', views.CartShowView.as_view(), name='cart-show'),
    path('cart/total/', views.CartTotalView.as_view(), name='cart-total'),
    path('item-order/add/', views.ItemOrderAddView.as_view(), name='item-order-add'),
    path('item-order/show/draft/', views.ItemOrderShowDraftView.as_view(), name='item-order-show-draft'),
]
