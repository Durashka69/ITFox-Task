from rest_framework import serializers

from mainapp.models import User, News, Like, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", 
            "username", 
            "email", 
            "is_staff",
            "is_superuser",
        )


class LikeSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    news_title = serializers.ReadOnlyField(source="news.title")

    class Meta:
        model = Like
        fields = (
            "id", 
            "user", 
            "username", 
            "news_title", 
            'news',
            "date"
        )

        extra_kwargs = {
            "user": {"read_only": True}, 
            "news": {"write_only": True}
        }


class NewsLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Like
        fields = (
            'user',
            'date'
        )


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    news_title = serializers.ReadOnlyField(source="news.title")

    class Meta:
        model = Comment
        fields = (
            "id", 
            "user", 
            "username", 
            "news_title",
            'news',
            "content", 
            "date"
        )

        extra_kwargs = {
            "user": {"read_only": True}, 
            "news": {"write_only": True}
        }


class NewsCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Comment
        fields = (
            'user',
            'content',
            'date'
        )


class NewsSerializer(serializers.ModelSerializer):
    likes = NewsLikeSerializer(
        many=True, read_only=True
    )
    comments = NewsCommentSerializer(
        many=True, read_only=True
    )
    username = serializers.ReadOnlyField(
        source="user.username"
    )

    class Meta:
        model = News
        fields = (
            "id",
            "user",
            "username",
            "title",
            "content",
            "image",
            "date",
            "total_likes",
            "likes",
            "total_comments",
            "comments",
        )

        extra_kwargs = {"user": {"read_only": True}}
