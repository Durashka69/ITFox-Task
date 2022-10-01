from rest_framework.routers import DefaultRouter

from mainapp.views import (
    UserViewSet,
    LikeViewSet,
    NewsViewSet,
    CommentViewSet
)


router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('likes', LikeViewSet, basename='likes')
router.register('comments', CommentViewSet, basename='comments')
router.register('news', NewsViewSet, basename='news')

urlpatterns = []

urlpatterns += router.urls
