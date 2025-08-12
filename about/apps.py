"""
App configuration for the About app.
"""

from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration for the About app.
    Sets default auto field and app name.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "about"
