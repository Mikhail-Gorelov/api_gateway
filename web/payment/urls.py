from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'payment'

router = DefaultRouter()

urlpatterns = [

]

urlpatterns += router.urls
