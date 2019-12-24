from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.db.models import CharField
from django.db.models import Model
from django.db.models import ForeignKey
from django.db.models import CASCADE

from .managers import FriendshipManager


class Friendship(Model):
    """
    Represent two users as friends

    The model instance is created when a user sends a request to another user
    The model instance is deleted when two users cancel their friendship

    Attrs:
        user_from (user): a user initiator
        user_to (user): a user that replies to the offer
        status (choice): friendship status
            choices:
                waiting for reply
                friends
    """
    WAITING_FOR_REPLY = 'WR'
    FRIENDS = 'FR'
    STATUS_CHOICES = [
        (WAITING_FOR_REPLY, _('Waiting for reply')),
        (FRIENDS, _('Friends'))
    ]

    user_from = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name='init_friendship',
        verbose_name=_('Initiator')
    )
    user_to = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name='replied_friendship',
        verbose_name=_('Replier')
    )
    status = CharField(
        _('Friendship status'),
        max_length=2,
        choices=STATUS_CHOICES,
        default=WAITING_FOR_REPLY
    )

    objects = FriendshipManager()

    def is_active(self):
        return self.status == self.FRIENDS

    def __str__(self):
        """String representation"""
        return f'{self.user_from} - {self.user_to}'

    class Meta:
        verbose_name = _('friendship')
        verbose_name_plural = _('friendships')
