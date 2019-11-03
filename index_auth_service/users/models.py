from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


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

    def get_absolute_url(self):
        return reverse(
            "users:detail",
            kwargs={
                "username": self.username
            }
        )
