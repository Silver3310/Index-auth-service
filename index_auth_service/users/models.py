from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from django.db.models import CharField

from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from .managers import CustomUserManager


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
        avatar (image): a user's avatar of 980*980 size
        avatar_thumbnail (image): a small version of avatar, 40*40
    """

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(
        _("Name of User"),
        blank=True,
        max_length=255
    )
    avatar = ProcessedImageField(
        verbose_name=_("User avatar"),
        upload_to='user_avatars',
        processors=[ResizeToFill(980, 980)],
        format='JPEG',
        blank=True,
    )
    avatar_thumbnail = ImageSpecField(
        source='avatar',
        processors=[ResizeToFill(40, 40)],
        format='JPEG',
        options={'quality': 60},
    )

    objects = CustomUserManager()

    def get_absolute_url(self):
        return reverse(
            "users:detail",
            kwargs={
                "username": self.username
            }
        )
