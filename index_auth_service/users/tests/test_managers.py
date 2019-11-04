import pytest
from django.conf import settings

from index_auth_service.users.models import User
from index_auth_service.users.models import Friendship

from .factories import FriendshipFactory

pytestmark = pytest.mark.django_db


class TestUserManager:
    def test_get_users(
        self,
        user: settings.AUTH_USER_MODEL
    ):
        assert user not in User.objects.get_queryset().get_users(user)


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
