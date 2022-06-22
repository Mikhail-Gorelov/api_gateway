from django.urls import path, include

app_name = 'v1'


urlpatterns = [
    path('', include('api.v1.auth_microservice.urls')),
    path('', include('api.v1.products_microservice.urls')),
    path('', include('api.v1.cart_microservice.urls')),
]

