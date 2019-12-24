import pytest

from index_auth_service.friends.models import Friendship
from index_auth_service.friends.tests.factories import FriendshipFactory

pytestmark = pytest.mark.django_db


def test_friendship_creations():
    """Check if friendships are created without any surprise"""
    FriendshipFactory()
    assert Friendship.objects.count() == 1
    assert Friendship.objects.first().status == Friendship.WAITING_FOR_REPLY
