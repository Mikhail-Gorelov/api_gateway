from django.conf import settings

from main.services import CeleryProductsService
from django.core.cache import cache
from src.celery import app


@app.task
def cache_active_channels():
    service = CeleryProductsService(url=f"{settings.CHANNEL_SETTINGS['ACTIVE_CHANNELS_URL']}")
    response = service.service_response(method="get")
    cache_key = cache.make_key(settings.CHANNEL_SETTINGS["CACHE_ACTIVE_CHANNELS_KEY"])
    cache.set(
        cache_key,
        response.data.get('results'),
        timeout=settings.CHANNEL_SETTINGS['CACHE_ACTIVE_CHANNELS_TIMEOUT']
    )
