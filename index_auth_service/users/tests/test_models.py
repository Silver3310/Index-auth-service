import pytest
from django.conf import settings

from index_auth_service.users.models import Friendship
from index_auth_service.users.tests.factories import FriendshipFactory

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: settings.AUTH_USER_MODEL):
    assert user.get_absolute_url() == f"/users/{user.username}/"


@pytest.mark.django_db
def test_friendship_creations():
    """Check if friendships are created without any surprise"""
    FriendshipFactory()
    assert Friendship.objects.count() == 1
    assert Friendship.objects.first().status == Friendship.WAITING_FOR_REPLY

