import pytest
from django.conf import settings

from index_auth_service.users.models import User

pytestmark = pytest.mark.django_db


class TestUserManager:
    def test_get_users(
        self,
        user: settings.AUTH_USER_MODEL
    ):
        assert user not in User.objects.get_queryset().get_users(user)
