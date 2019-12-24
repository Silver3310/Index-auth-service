import pytest
from django.conf import settings

from index_auth_service.friends.models import Friendship

from .factories import FriendshipFactory

pytestmark = pytest.mark.django_db


class TestFriendshipManager:
    def test_find_friends(
        self,
        user: settings.AUTH_USER_MODEL
    ):
        FriendshipFactory(user_to=user)
        FriendshipFactory(user_from=user)

        # check that filtering works correctly for all items
        assert all(
            user == friends.user_to or user == friends.user_from
            for friends in Friendship.objects.get_queryset().find_friends(user)
        )
