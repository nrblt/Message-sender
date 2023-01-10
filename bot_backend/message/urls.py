from rest_framework.routers import SimpleRouter

from .views import MessageViewSet

router = SimpleRouter()
router.register("",MessageViewSet)

urlpatterns = router.urls
