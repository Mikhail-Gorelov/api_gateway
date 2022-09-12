from main.services import get_active_channels
from src.celery import app


@app.task
def cache_active_channels():
    get_active_channels()
