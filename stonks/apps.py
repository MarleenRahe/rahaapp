from django.apps import AppConfig
from .data_methods import load_data, data


class StonksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stonks'

    def ready(self):
        load_data()
        print(data)
