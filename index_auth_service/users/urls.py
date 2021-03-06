from django.urls import path

from .views import user_redirect_view
from .views import user_update_view
from .views import user_detail_view
from .views import user_list_view


app_name = "users"
urlpatterns = [
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
]
