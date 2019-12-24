from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from .models import Friendship

User = get_user_model()


class FriendshipListView(LoginRequiredMixin, ListView):
    """
    List all the user's friends
    """

    model = Friendship
    template_name = 'friends/friends_list.html'

    def get_queryset(self):
        """Get all the user's friends"""
        return super().get_queryset().find_friends(self.request.user)


friendship_list_view = FriendshipListView.as_view()


def add_friend(
    request,
    pk: str
):
    """
    Add a friend to a user
    """

    # create a friendship object
    Friendship.objects.make_user_friend(
        request.user,
        User.objects.get(pk=int(pk))
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
