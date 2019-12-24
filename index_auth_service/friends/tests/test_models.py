import pytest

from index_auth_service.friends.models import Friendship
from index_auth_service.friends.tests.factories import FriendshipFactory

pytestmark = pytest.mark.django_db


def test_friendship_creations():
    """Check if friendships are created without any surprise"""
    friendship: Friendship = FriendshipFactory()
    assert Friendship.objects.count() == 1
    assert friendship.status == Friendship.WAITING_FOR_REPLY
    assert friendship.is_active() is False
    assert str(friendship) == f'{friendship.user_from} - {friendship.user_to}'
