from django.urls import path
from . import views
from .views import TokenRefreshView

app_name = 'auth_microservice'

urlpatterns = [
    path('sign-in/', views.LoginView.as_view(), name='sign-in'),
    path('sign-up/email/', views.SignUpEmailView.as_view(), name='sign-up-email'),
    path('sign-up/phone/', views.SignUpPhoneView.as_view(), name='sign-up-email'),
    path('verify-email/', views.VerifyEmailView.as_view(), name='verify-email'),
    path('password/reset/', views.PasswordResetView.as_view(), name='password-reset'),
    path('password/reset/confirm/', views.PasswordResetConfirmView.as_view(), name='password-reset-confirm-email'),
    path('refresh-jwt/', TokenRefreshView.as_view(), name='refresh-jwt'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user-profile/', views.GetUserView.as_view(), name='get_user')
]
