from django.apps import AppConfig


class TyuusennConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tyuusenn"

    def ready(self):
        from .views import start

        start()
