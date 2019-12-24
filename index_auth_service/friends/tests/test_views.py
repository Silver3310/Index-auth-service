import pytest
from django.conf import settings
from django.test import RequestFactory

from index_auth_service.friends.views import FriendshipListView

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
