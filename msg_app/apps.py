from django.apps import AppConfig


class MsgAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "msg_app"

    def ready(self):
        from msg_app import signals  # noqa
