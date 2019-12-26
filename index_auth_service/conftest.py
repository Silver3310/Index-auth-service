import pytest
from django.conf import settings
from django.test import RequestFactory

from index_auth_service.users.tests.factories import UserFactory
from index_auth_service.friends.tests.factories import FriendshipFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()


@pytest.fixture
def user_friend(
    user: settings.AUTH_USER_MODEL
) -> settings.AUTH_USER_MODEL:
    """
    Create a friendship and return a friend
    """
    user_friend = UserFactory()
    FriendshipFactory(
        user_to=user,
        user_from=user_friend
    )
    return user_friend


@pytest.fixture()
def user_to_login_username(
    client,
    django_user_model
) -> str:
    """
    Create a user without hashing a password (so we can use it for login and
    return the user's username)
    """
    username = "user1"
    password = "bar"
    django_user_model.objects.create_user(
        username=username,
        password=password
    )  # no user factory so the pass is not hashed
    client.login(
        username=username,
        password=password
    )
    return username


@pytest.fixture()
def user_to_login(
    client,
    django_user_model
) -> settings.AUTH_USER_MODEL:
    """
    Create a user without hashing a password (so we can use it for login and
    return the user)
    """
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(
        username=username,
        password=password
    )  # no user factory so the pass is not hashed
    client.login(
        username=username,
        password=password
    )
    return user

