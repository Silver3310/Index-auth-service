import pytest
from django.conf import settings

from index_auth_service.friends.models import Friendship

from index_auth_service.users.tests.factories import UserFactory
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

    def test_make_user_friend(
        self,
        user: settings.AUTH_USER_MODEL
    ):
        friends: Friendship = Friendship.objects.make_user_friend(
            user,
            UserFactory()
        )

        assert friends.status == Friendship.WAITING_FOR_REPLY

    def test_get_user_friend(
        self,
        user: settings.AUTH_USER_MODEL,
        user_friend: settings.AUTH_USER_MODEL
    ):
        assert Friendship.objects.get_user_friend(
            user_to=user,
            user_from=user_friend
        ) == Friendship.objects.get(
            user_to=user,
            user_from=user_friend
        )

    def test_approve_user_fried(
        self,
        user: settings.AUTH_USER_MODEL,
        user_friend: settings.AUTH_USER_MODEL
    ):
        Friendship.objects.approve_user_friend(
            user_to=user,
            user_from=user_friend
        )

        assert Friendship.objects.get_user_friend(
            user_to=user,
            user_from=user_friend
        ).status == Friendship.FRIENDS

    def test_delete_user_friend(
        self,
        user: settings.AUTH_USER_MODEL,
        user_friend: settings.AUTH_USER_MODEL
    ):
        Friendship.objects.delete_user_friend(
            user_to=user,
            user_from=user_friend
        )

        assert Friendship.objects.get_user_friend(
            user_to=user,
            user_from=user_friend
        ) is None
