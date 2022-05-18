from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'auth_microservice'

urlpatterns = [
    path('sign-in/', views.LoginView.as_view(), name='sign-in'),
]
