from django import forms
from rest_framework import serializers

from blog.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content', 'created_at')


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'comments']
        # fields = '__all__'
