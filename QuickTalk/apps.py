from django.apps import AppConfig


class QuicktalkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'QuickTalk'

def ready(self):
    import QuickTalk.signals

    