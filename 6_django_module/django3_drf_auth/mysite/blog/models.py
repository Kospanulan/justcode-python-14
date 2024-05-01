from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Category(models.Model):

    name = models.CharField(verbose_name="Название", max_length=100, unique=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"{self.name} ({self.pk})"


class Post(models.Model):

    title = models.CharField(verbose_name="Заголовок", max_length=200, db_index=True)
    content = models.TextField(verbose_name="Текст статьи", blank=True, null=True)

    photo = models.ImageField(verbose_name="Аватар", upload_to='images/', blank=True, null=True)

    author = models.ForeignKey(get_user_model(), verbose_name="Автор", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Категории", blank=True, null=True)

    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Время обновления", auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.pk})"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

        ordering = ['-created_at']
        unique_together = ('title', 'content')
        indexes = [
            models.Index(fields=['title', 'content']),  # compound indexes
        ]
        default_related_name = 'posts'


class Comment(models.Model):

    post = models.ForeignKey(Post, verbose_name="Статья", on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), verbose_name="Автор", on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(verbose_name="Комментарий")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content} ({self.pk})"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

