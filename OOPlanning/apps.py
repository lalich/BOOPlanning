# OOPlanning/apps.py

from django.apps import AppConfig

class OoplanningConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OOPlanning'

    def ready(self):
        import OOPlanning.signals
