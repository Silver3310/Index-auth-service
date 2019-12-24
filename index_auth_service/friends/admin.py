from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Friendship

User = get_user_model()


@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    """Friendship for the admin panel"""

    list_display = [
        "pk",
        "user_from",
        "user_to",
        "status"
    ]
    search_fields = [
        "user_from",
        "user_to",
        "status"
    ]
