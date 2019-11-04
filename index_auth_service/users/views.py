from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.db.models import Q
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from .models import Friendship

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    """
    Show the user's info
    """

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update the user's name
    """

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse(
            "users:detail",
            kwargs={
                "username": self.request.user.username
            }
        )

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO,
            _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    """
    Redirect to the detailed user page
    """

    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail",
            kwargs={
                "username": self.request.user.username
            }
        )


user_redirect_view = UserRedirectView.as_view()


class UserListView(LoginRequiredMixin, ListView):
    """
    List all users to observe their profiles and send friend requests
    """

    model = User
    template_name = 'users/user_list.html'

    def get_queryset(self):
        """Exclude the user"""
        return super().get_queryset().get_users(self.request.user)


user_list_view = UserListView.as_view()


class FriendshipListView(LoginRequiredMixin, ListView):
    """
    List all the user's friends
    """

    model = Friendship
    template_name = 'users/friends_list.html'

    def get_queryset(self):
        """Get all the user's friends"""
        return super().get_queryset().find_friends(self.request.user)


friendship_list_view = FriendshipListView.as_view()
