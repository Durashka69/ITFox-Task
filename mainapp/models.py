from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class News(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название новости'
    )
    content = models.TextField(
        verbose_name='Содержание'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )

    @property
    def total_likes(self) -> int:
        return self.likes.all().count()

    @property
    def total_comments(self) -> int:
        return self.comments.all().count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='likes'
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Новость',
        related_name='likes'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )

    def __str__(self):
        return f'Лайк пользователя {self.user.username} на пост {self.news.title}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='comments'
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Новость',
        related_name='comments'
    )
    content = models.TextField(
        verbose_name = 'Содержание'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )

    def __str__(self):
        return f'Лайк пользователя {self.user.username} на пост {self.news.title} {self.date}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
