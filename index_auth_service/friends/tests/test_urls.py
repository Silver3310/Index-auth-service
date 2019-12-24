import pytest
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_friends():
    assert reverse("friends:friends") == "/friends/"
    assert resolve("/friends/").view_name == "friends:friends"
