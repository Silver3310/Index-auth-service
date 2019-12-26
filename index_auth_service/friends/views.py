from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.generic import ListView

from .models import Friendship

from .tasks import send_email

User = get_user_model()


class FriendshipListView(LoginRequiredMixin, ListView):
    """
    List all the user's friends
    """

    model = Friendship
    paginate_by = 10
    template_name = 'friends/friends_list.html'

    def get_queryset(self):
        """Get all the user's friends"""
        return super().get_queryset().find_friends(self.request.user)


friendship_list_view = FriendshipListView.as_view()


def send_mail_friend_request(
    user: settings.AUTH_USER_MODEL,
    user_friend: settings.AUTH_USER_MODEL
):
    """
    Prepare data to be sent to a user
    """
    title: str = "PrivetThere: New friend!"
    body: str = "The user '{username}' ({link}) would like to add you as a " \
                "friend.\nYou can approve or refuse your friendship on the " \
                "website. See you there :)".format(
                    username=user.username,
                    link=settings.HOST_ADDRESS + user_friend.get_absolute_url()
                )

    send_email.delay(
        title=title,
        body=body,
        email=user_friend.email
    )


def add_friend(
    request,
    pk: str
):
    """
    Add a friend to a user
    """

    user_friend: settings.AUTH_USER_MODEL = User.objects.get(pk=int(pk))
    # create a friendship object
    Friendship.objects.make_user_friend(
        request.user,
        user_friend
    )

    send_mail_friend_request(
        user=request.user,
        user_friend=user_friend
    )

    return HttpResponseRedirect(
        reverse(
            'users:list',
        )
    )


def delete_friend(
    request,
    pk: str
):
    """
    Delete a friend request or friendship
    """

    Friendship.objects.delete_user_friend(
        request.user,
        User.objects.get(pk=int(pk))
    )

    # return to the friends page if the request was from there
    if 'friends' in request.GET:
        return HttpResponseRedirect(
            reverse('friends:friends')
        )

    return HttpResponseRedirect(
        reverse('users:list')
    )


def approve_friend(
    request,
    pk: str
):
    """
    Approve a friend request
    """

    Friendship.objects.approve_user_friend(
        user_to=request.user,
        user_from=User.objects.get(pk=int(pk))
    )

    # return to the friends page if the request was from there
    if 'friends' in request.GET:
        return HttpResponseRedirect(
            reverse('friends:friends')
        )

    return HttpResponseRedirect(
        reverse('users:list')
    )
