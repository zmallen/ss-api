from django.apps import AppConfig


class SsapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ssapi'
    def ready(self):
        from ssapi import signals
