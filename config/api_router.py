from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from todo_app.users.api.views import UserViewSet
from items.views import ListContainerViewSet, ListItemViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("containers", ListContainerViewSet, basename=r'containers')
router.register("items", ListItemViewSet, basename=r'items')


app_name = "api"
urlpatterns = router.urls
