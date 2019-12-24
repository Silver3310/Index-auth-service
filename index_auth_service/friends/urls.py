from django.urls import path

from .views import friendship_list_view
from .views import add_friend
from .views import delete_friend
from .views import approve_friend


app_name = "friends"
urlpatterns = [
    path(
        "",
        view=friendship_list_view,
        name="friends"
    ),
    path(
        "add/<int:pk>/",
        view=add_friend,
        name="add_friend"
    ),
    path(
        "del/<int:pk>/",
        view=delete_friend,
        name="delete_friend"
    ),
    path(
        "app/<int:pk>/",
        view=approve_friend,
        name="approve_friend"
    )
]
