from rest_framework.routers import SimpleRouter
from django.urls import path

from board.views import PostViewSet

router = SimpleRouter()
router.register('posts', PostViewSet, basename='post')

urlpatterns = router.urls
