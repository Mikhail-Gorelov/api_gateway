from django.urls import path
from . import views
from .views import TokenRefreshView

app_name = 'auth_microservice'

urlpatterns = [
    path('sign-in/email/', views.LoginEmailView.as_view(), name='sign-in-email'),
    path('sign-in/phone/', views.LoginPhoneView.as_view(), name='sign-in-phone'),
    path('sign-up/email/', views.SignUpEmailView.as_view(), name='sign-up-email'),
    path('sign-up/phone/', views.SignUpPhoneView.as_view(), name='sign-up-email'),
    path('verify-user/', views.VerifyView.as_view(), name='verify-user'),
    path('password/reset/email/', views.PasswordResetEmailView.as_view(), name='password-reset-email'),
    path('password/reset/phone/', views.PasswordResetPhoneView.as_view(), name='password-reset-phone'),
    path('password/reset/confirm/', views.PasswordResetConfirmView.as_view(), name='password-reset-confirm-email'),
    path('refresh-jwt/', TokenRefreshView.as_view(), name='refresh-jwt'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user-profile/', views.GetUserView.as_view(), name='get_user'),
    path('user-profile/set-password/', views.ChangeUserPasswordView.as_view(), name='set-password'),
    path('user-profile/change/', views.ChangeUserProfileView.as_view(), name='change-profile'),
    path('default-address/billing/change/', views.ChangeBillingAddressView.as_view(), name='change-billing-address'),
    path('default-address/shipping/change/', views.ChangeShippingAddressView.as_view(), name='change-shipping-address'),
]
