from django.contrib.auth.models import UserManager

from django.db.models import Manager
from django.db.models import QuerySet
from django.db.models import Q


class UserQuerySet(QuerySet):
    """
    Custom queryset for User
    """

    def get_users(self, user):
        """Get all users but the user that requests this info"""
        return self.exclude(pk=user.pk)


class CustomUserManager(UserManager):
    """
    Custom manager for User
    """

    def get_queryset(self):
        """Make it possible to use custom queryset methods"""
        return UserQuerySet(self.model, using=self._db)


class FriendshipQuerySet(QuerySet):
    """
    Queryset for the Friendship model
    """

    def find_friends(self, user):
        """Find all the friends for the user"""
        return self.filter(Q(user_from=user) | Q(user_to=user)).order_by('status')


class FriendshipManager(Manager):
    """
    Custom manager for the Friendship model
    """

    def get_queryset(self):
        """Make it possible to use custom queryset methods"""
        return FriendshipQuerySet(self.model, using=self._db)
