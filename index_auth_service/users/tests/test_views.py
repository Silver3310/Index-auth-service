import pytest
from django.conf import settings
from django.test import RequestFactory

from index_auth_service.users.views import UserRedirectView
from index_auth_service.users.views import UserUpdateView
from index_auth_service.users.views import UserListView
from index_auth_service.users.views import FriendshipListView
from index_auth_service.users.models import Friendship

from .factories import FriendshipFactory

pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    def test_get_success_url(
        self,
        user: settings.AUTH_USER_MODEL,
        request_factory: RequestFactory
    ):
        view = UserUpdateView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/users/{user.username}/"

    def test_get_object(
        self,
        user: settings.AUTH_USER_MODEL,
        request_factory: RequestFactory
    ):
        view = UserUpdateView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user


class TestUserRedirectView:
    def test_get_redirect_url(
        self,
        user: settings.AUTH_USER_MODEL,
        request_factory: RequestFactory
    ):
        view = UserRedirectView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_redirect_url() == f"/users/{user.username}/"


class TestUserListView:
    def test_get_queryset(
        self,
        user: settings.AUTH_USER_MODEL,
        request_factory: RequestFactory
    ):
        view = UserListView()
        request = request_factory.get('/fake-url/')
        request.user = user

        view.request = request

        assert user not in view.get_queryset()


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
