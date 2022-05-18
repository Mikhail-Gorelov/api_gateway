from django.conf import settings
from microservice_request.services import ConnectionService

class AuthorizationService(ConnectionService):
    service = settings.AUTHORIZATION_API_URL
