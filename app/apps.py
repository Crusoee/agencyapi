from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

from django.apps import AppConfig
class MyAppConfig(AppConfig):
    name = 'app'
    verbose_name = "My Application"
    def ready(self):
        pass # startup code here