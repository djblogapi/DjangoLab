from django.urls import include, path

from rest_framework import routers
from user.views import FileViewSet

app_name = "user"

router = routers.SimpleRouter()
router.register("file", FileViewSet, basename="file")

urlpatterns = [
    path("", include(router.urls)),
]
