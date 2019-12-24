from django.contrib.auth import get_user_model

from django.db.models import ObjectDoesNotExist
from django.db.models import Manager
from django.db.models import QuerySet
from django.db.models import Q

User = get_user_model()


class FriendshipQuerySet(QuerySet):
    """
    Queryset for the Friendship model
    """

    def find_friends(
        self,
        user: User
    ):
        """Find all the friends for the user"""
        return self.filter(
            Q(user_from=user) | Q(user_to=user)
        ).order_by('status')


class FriendshipManager(Manager):
    """
    Custom manager for the Friendship model
    """

    def get_queryset(self):
        """Make it possible to use custom queryset methods"""
        return FriendshipQuerySet(self.model, using=self._db)

    def get_user_friend(
        self,
        user_from: User,
        user_to: User
    ):
        try:
            friends = self.get(
                Q(user_from=user_from, user_to=user_to) |
                Q(user_to=user_from, user_from=user_to)
            )
        except ObjectDoesNotExist:
            return None
        return friends

    def make_user_friend(
        self,
        user_from: User,
        user_to: User
    ):
        """Make a friend request from a user with a pk user"""
        friends = self.create(
            user_from=user_from,
            user_to=user_to
        )
        return friends

    def delete_user_friend(
        self,
        user_from: User,
        user_to: User
    ):
        """Delete a friend request or friendship"""
        friends = self.get(
            Q(user_from=user_from, user_to=user_to) |
            Q(user_to=user_from, user_from=user_to)
        )
        friends.delete()

    def approve_user_friend(
        self,
        user_from: User,
        user_to: User
    ):
        """Approve a friend request or friendship"""
        friends = self.get(
            user_from=user_from,
            user_to=user_to
        )
        friends.status = 'FR'
        friends.save()
