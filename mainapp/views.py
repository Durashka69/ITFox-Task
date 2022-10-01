from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser

from mainapp.models import User, Like, Comment, News

from mainapp.serializers import (
    LikeSerializer, 
    CommentSerializer,
    NewsSerializer,
    UserSerializer
)
from mainapp.permissions import IsOwnerOrAdminOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class NewsViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
