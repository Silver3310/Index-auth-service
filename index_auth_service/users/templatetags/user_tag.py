from django import template
from django.contrib.auth import get_user_model

from index_auth_service.users.models import Friendship

register = template.Library()
User = get_user_model()


@register.simple_tag(takes_context=True)
def get_friend(context, pk: str):
    """Get a status of friendship"""
    return Friendship.objects.get_user_friend(
        context['request'].user,
        User.objects.get(pk=int(pk))
    )
