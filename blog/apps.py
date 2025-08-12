from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration for the blog app.
    Sets default auto field and imports signals on app ready.
    """
    name = 'blog'
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        # Import signal handlers to connect model signals
        import blog.signals
