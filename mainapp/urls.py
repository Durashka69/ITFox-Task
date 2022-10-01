from rest_framework.routers import SimpleRouter

from mainapp.views import (
    UserViewSet,
    LikeViewSet,
    NewsViewSet,
    CommentViewSet
)


router = SimpleRouter()

router.register('users', UserViewSet, basename='users')
router.register('likes', LikeViewSet, basename='likes')
router.register('comments', CommentViewSet, basename='comments')
router.register('news', NewsViewSet, basename='news')

urlpatterns = []

urlpatterns += router.urls
