from django.contrib import admin

# Register your models here.
from django.apps import AppConfig
class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.auth'
    label = 'core_auth'