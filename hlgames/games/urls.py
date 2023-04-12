from rest_framework import routers
from django.urls import path, include, re_path

from games import views

router = routers.DefaultRouter()
router.register(r"platforms", views.PlatformViewSet)

urlpatterns = [
    path("", include(router.urls)),
    re_path(
        "games/",
        views.GameViewSet.as_view(),
        name="list_games",
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
