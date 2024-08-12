from django.apps import AppConfig



class JobsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobs'

    def ready(self):
        from .scheduler import start_scheduler
        start_scheduler()

