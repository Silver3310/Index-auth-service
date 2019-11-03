from typing import Any, Sequence

from django.contrib.auth import get_user_model

from factory import DjangoModelFactory
from factory import Faker
from factory import post_generation
from factory import SubFactory

from index_auth_service.users.models import Friendship


class UserFactory(DjangoModelFactory):
    """Factory for the user model"""

    username = Faker("user_name")
    email = Faker("email")
    name = Faker("name")

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = Faker(
            "password",
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(extra_kwargs={})
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]


class FriendshipFactory(DjangoModelFactory):
    """Factory for the friendship model"""

    user_from = SubFactory(UserFactory)
    user_to = SubFactory(UserFactory)

    class Meta:
        model = Friendship
