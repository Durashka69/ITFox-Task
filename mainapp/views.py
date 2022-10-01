from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

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
    permission_classes = (IsAdminUser,)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdminOrReadOnly,)

    def create(self, request, *args, **kwargs):
        if Like.objects.filter(
            user=self.request.user,
            news=request.data.get('news')
        ):
            return Response(
                {'error': f'Like from {request.user.username} already exists!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdminOrReadOnly)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrAdminOrReadOnly)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
