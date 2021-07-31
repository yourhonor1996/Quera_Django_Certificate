from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    
    def ready(self) -> None:
        import accounts.signals
