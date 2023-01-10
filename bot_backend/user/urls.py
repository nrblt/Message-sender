from rest_framework.routers import SimpleRouter

from .views import UserAndChatViewSet

router = SimpleRouter()
router.register("",UserAndChatViewSet)

urlpatterns = router.urls
