from django import template
from django.contrib.auth import get_user_model
from django.conf import settings

from index_auth_service.friends.models import Friendship

register = template.Library()
User = get_user_model()


@register.simple_tag(takes_context=True)
def get_friend(context, pk: str):
    """Get a status of friendship"""
    return Friendship.objects.get_user_friend(
        context['request'].user,
        User.objects.get(pk=int(pk))
    )


@register.simple_tag(takes_context=False)
def get_default_avatar():
    """Return a default image for avatar"""
    return settings.DEFAULT_AVATAR_IMAGE


@register.simple_tag(takes_context=False)
def get_default_thumbnail_avatar():
    """Return a default image for avatar"""
    return settings.DEFAULT_AVATAR_IMAGE_THUMBNAIL
