from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'auth_microservice'

router = DefaultRouter()

urlpatterns = [

]

urlpatterns += router.urls
