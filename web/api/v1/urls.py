from django.urls import path, include

app_name = 'v1'


urlpatterns = [
    path('', include('api.v1.auth_microservice.urls')),
]

