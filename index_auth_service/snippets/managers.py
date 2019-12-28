from django.conf import settings

from django.db.models import Manager
from django.db.models import Q
from django.db.models import When
from django.db.models import Case
from django.db.models import Value
from django.db.models import IntegerField


class SnippetManager(Manager):
    """
    Custom manager for the Snippet model
    """

    def get_snippets(
        self,
        user: settings.AUTH_USER_MODEL
    ):
        """
        Don't show the snippets that are hidden and don't belong to a user and
        sort the snippet so the first snippets belong to a user
        """
        return self.filter(
            Q(user=user) | Q(is_visible=True)
        ).annotate(
            first_user=Case(
                When(user=user, then=Value(1)),
                default=Value(0),
                output_field=IntegerField()
            )
        ).order_by('-first_user')
