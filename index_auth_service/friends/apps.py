from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FriendsConfig(AppConfig):
    name = "index_auth_service.friends"
    verbose_name = _("Friends")

    def ready(self):
        try:
            import index_auth_service.friends.signals  # noqa F401
        except ImportError:
            pass
