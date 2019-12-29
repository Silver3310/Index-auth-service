from django.contrib import admin

from .models import Snippet


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    """
    Show the snippet model in the admin panel
    """

    list_display = [
        "__str__",
        "is_visible"
    ]
    search_fields = ["code"]
    list_filter = ["is_visible"]
