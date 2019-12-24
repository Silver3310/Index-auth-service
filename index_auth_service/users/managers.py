from django.contrib.auth.models import UserManager

from django.db.models import QuerySet


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

