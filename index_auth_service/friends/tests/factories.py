from factory import DjangoModelFactory
from factory import SubFactory

from index_auth_service.users.tests.factories import UserFactory
from index_auth_service.friends.models import Friendship


class FriendshipFactory(DjangoModelFactory):
    """Factory for the friendship model"""

    user_from = SubFactory(UserFactory)
    user_to = SubFactory(UserFactory)

    class Meta:
        model = Friendship
