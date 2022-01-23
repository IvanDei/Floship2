from django.apps import AppConfig


class AppWhConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_wh'

    def ready(self):
        import app_wh.signals