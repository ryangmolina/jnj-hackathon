from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'app.accounts'

    def ready(self):
        from .signals import register_handlers
        register_handlers()
