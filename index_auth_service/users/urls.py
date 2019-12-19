from django.urls import path

from .views import user_redirect_view
from .views import user_update_view
from .views import user_detail_view
from .views import user_list_view
from .views import friendship_list_view
from .views import add_friend
from .views import delete_friend
from .views import approve_friend


app_name = "users"
urlpatterns = [
    # users
    path(
        "~redirect/",
        view=user_redirect_view,
        name="redirect"
    ),
    path(
        "~update/",
        view=user_update_view,
        name="update"
    ),
    path(
        "~list/",
        view=user_list_view,
        name="list"
    ),
    path(
        "~detail/<str:username>/",
        view=user_detail_view,
        name="detail"
    ),
    # friends
    path(
        "~friends/",
        view=friendship_list_view,
        name="friends"
    ),
    path(
        "~friend/add/<int:pk>/",
        view=add_friend,
        name="add_friend"
    ),
    path(
        "~friend/del/<int:pk>/",
        view=delete_friend,
        name="delete_friend"
    ),
    path(
        "~friend/app/<int:pk>/",
        view=approve_friend,
        name="approve_friend"
    )
]
