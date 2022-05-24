from django.urls import path
from . import views

app_name = 'auth_microservice'

urlpatterns = [
    path('sign-in/', views.LoginView.as_view(), name='sign-in'),
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('verify-email/', views.VerifyEmailView.as_view(), name='verify-email'),
    path('password/reset/', views.PasswordResetView.as_view(), name='password-reset'),
    path('password/reset/confirm/', views.PasswordResetConfirmView.as_view(), name='password-reset-confirm-email'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
