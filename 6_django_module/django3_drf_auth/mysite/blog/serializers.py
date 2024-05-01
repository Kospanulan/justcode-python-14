from django import forms
from rest_framework import serializers

from blog.models import Post, Comment, Category


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('pk', 'name', 'description')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('pk', 'content', 'created_at')


class PostListCreateSerializer(serializers.ModelSerializer):

    comments_count = serializers.IntegerField(read_only=True)
    categories = CategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'pk', 'title', 'content', 'photo',
            'author_id', 'created_at', 'updated_at',
            'comments_count', 'categories'
        ]


class PostRetrieveUpdateDestroySerializer(serializers.ModelSerializer):

    # categories = CategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'title', 'content', 'photo',
            'author_id', 'categories', 'created_at', 'updated_at',
        ]

