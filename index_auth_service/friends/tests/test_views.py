import pytest

from django.conf import settings
from django.test import RequestFactory
from django.urls import reverse

from index_auth_service.friends.views import FriendshipListView
from index_auth_service.friends.models import Friendship

from .factories import FriendshipFactory

pytestmark = pytest.mark.django_db


class TestFriendshipListView:
    def test_get_queryset(
        self,
        user: settings.AUTH_USER_MODEL,
        request_factory: RequestFactory
):
        view = FriendshipListView()
        request = request_factory.get('/fake-url/')
        request.user = user

        # create two friendships, the second user is created automatically
        FriendshipFactory(user_to=request.user)
        FriendshipFactory(user_from=request.user)

        view.request = request

        # check that filtering works correctly for all items
        assert all(
            request.user == friends.user_to
            or request.user == friends.user_from
            for friends in view.get_queryset()
        )

    def test_add_friend(
        self,
        client,
        user: settings.AUTH_USER_MODEL,
        user_to_login: settings.AUTH_USER_MODEL
    ):
        client.get(
            reverse(
                'friends:add_friend',
                kwargs={
                    'pk': user.pk
                }
            )
        )
        friendship: Friendship = Friendship.objects.get_user_friend(
            user_from=user_to_login,
            user_to=user
        )

        assert friendship is not None
        assert friendship.status == friendship.WAITING_FOR_REPLY

    def test_delete_friend(
        self,
        client,
        user: settings.AUTH_USER_MODEL,
        user_to_login: settings.AUTH_USER_MODEL
    ):
        Friendship.objects.create(
            user_from=user,
            user_to=user_to_login,
            status=Friendship.FRIENDS
        )

        client.get(
            reverse(
                'friends:delete_friend',
                kwargs={
                    'pk': user.pk
                }
            )
        )
        assert Friendship.objects.get_user_friend(
            user_from=user_to_login,
            user_to=user
        ) is None

    def test_approve_friend(
        self,
        client,
        user: settings.AUTH_USER_MODEL,
        user_to_login: settings.AUTH_USER_MODEL
    ):
        Friendship.objects.make_user_friend(
            user_from=user,
            user_to=user_to_login
        )

        client.get(
            reverse(
                'friends:approve_friend',
                kwargs={
                    'pk': user.pk
                }
            )
        )
        assert Friendship.objects.get_user_friend(
            user_from=user_to_login,
            user_to=user
        ).status == Friendship.FRIENDS
