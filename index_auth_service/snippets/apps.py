from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SnippetsConfig(AppConfig):
    name = "index_auth_service.snippets"
    verbose_name = _("Snippets")

    def ready(self):
        try:
            import index_auth_service.snippets.signals  # noqa F401
        except ImportError:
            pass
