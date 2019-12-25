import pytest
from celery.result import EagerResult

from index_auth_service.friends.tasks import send_email


@pytest.mark.django_db
def test_send_email(
    settings,
    user,
    user_friend
):
    """Show that our message is valid and returns True"""
    settings.CELERY_TASK_ALWAYS_EAGER = True

    title: str = "PrivetThere: New friend!"
    body: str = "The user '{username}' ({link}) would like to add you as a " \
                "friend.\nYou can approve or refuse your friendship on the " \
                "website. See you there :)".format(
                    username=user.username,
                    link=settings.HOST_ADDRESS + user_friend.get_absolute_url()
                )

    task_result = send_email.delay(
        title=title,
        body=body,
        email=user_friend.email
    )

    assert isinstance(task_result, EagerResult)
    assert task_result.result is True
