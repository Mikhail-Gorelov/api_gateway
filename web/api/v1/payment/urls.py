from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('webhooks/stripe/', views.StripeWebhookView.as_view(), name='stripe-webhook'),
    path('create-checkout-session/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
