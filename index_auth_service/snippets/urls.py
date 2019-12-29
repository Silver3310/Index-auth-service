from django.urls import path

from .views import snippet_detail_view
from .views import snippet_create_view
from .views import snippet_update_view
from .views import snippet_delete_view
from .views import snippet_list_view

from .search import snippet_search


app_name = "snippets"
urlpatterns = [
    path(
        "",
        view=snippet_list_view,
        name="snippets"
    ),
    path(
        "add/",
        view=snippet_create_view,
        name="create"
    ),
    path(
        "del/<int:pk>/",
        view=snippet_delete_view,
        name="delete"
    ),
    path(
        "info/<int:pk>/",
        view=snippet_detail_view,
        name="snippet"
    ),
    path(
        "upd/<int:pk>/",
        view=snippet_update_view,
        name="update"
    ),
    path(
        "search",
        view=snippet_search,
        name="search"
    )
]
