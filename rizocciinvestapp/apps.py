from django.apps import AppConfig


class RizocciinvestappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rizocciinvestapp'

    def ready(self):
    	import rizocciinvestapp.signals
