from django.apps import AppConfig


class StoreConfig(AppConfig):
     verbose_name = "Товары магазина"
     default_auto_field = 'django.db.models.BigAutoField'
     name = 'store'
