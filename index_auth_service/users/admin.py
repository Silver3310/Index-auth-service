from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from index_auth_service.users.forms import UserChangeForm
from index_auth_service.users.forms import UserCreationForm
from index_auth_service.users.models import Friendship

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
                    ("User", {"fields": ("name",)}),
                ) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


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
