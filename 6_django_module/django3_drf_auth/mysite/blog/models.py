from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.pk})"


class Post(models.Model):

    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField(blank=True, null=True)

    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def demo_content(self):
        return f"{self.content[:10]}..."

    def __str__(self):
        return f"{self.title} ({self.pk})"

    class Meta:
        ordering = ['title']
        unique_together = ('title', 'content')
        indexes = [
            models.Index(fields=['title', 'content']),  # compound indexes
        ]
        default_related_name = 'posts'


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content} ({self.pk})"


