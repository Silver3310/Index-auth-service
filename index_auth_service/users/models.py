from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.db.models import CharField
from django.db.models import Model
from django.db.models import ForeignKey
from django.db.models import CASCADE

from .managers import CustomUserManager
from .managers import FriendshipManager


class User(AbstractUser):
    """
    Custom user model

    Attrs:
        username (str): username
        name (str): replacement for first and last names
        first_name (str): first name
        last_name (str): last name
        email (str): email
        is_active (bool): if this user is active or not
        is_staff (bool): if this user is a member of staff or not
        date_joined (datetime): the datetime when user joined
    """

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(
        _("Name of User"),
        blank=True,
        max_length=255
    )

    objects = CustomUserManager()

    def get_absolute_url(self):
        return reverse(
            "users:detail",
            kwargs={
                "username": self.username
            }
        )


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
