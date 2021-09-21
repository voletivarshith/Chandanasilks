from django.apps import AppConfig


class ItemsappConfig(AppConfig):
    name = 'ItemsApp'
    def ready(self):
        import ItemsApp.signals