"""Snippet model

The model defined here lets users store their code snippets so this application
acts like a notebook for programmers
"""
from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from django.db.models import Model
from django.db.models import ForeignKey
from django.db.models import CASCADE
from django.db.models import TextField
from django.db.models import BooleanField

from .managers import SnippetManager


class Snippet(Model):
    """
    Snippet model (for code)

    Lets users store code snippets to use in the future

    Attrs:
        user (user): a user who owns a code snippet
        code (text): the code snippet itself
        is_visible (bool): whether this code snippet should be visible for
            others or not
    """

    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        verbose_name=_('Owner')
    )
    code = TextField(
        _("Code"),
        blank=True,
        max_length=255
    )
    is_visible = BooleanField(
        _("Visible for others"),
    )

    objects = SnippetManager()

    def get_absolute_url(self):
        return reverse(
            "snippets:snippet",
            kwargs={
                "pk": self.pk
            }
        )
