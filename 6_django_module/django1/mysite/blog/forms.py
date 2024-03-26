from django import forms
from django.contrib.auth import get_user_model

from blog.models import Post


class CreatePostForm(forms.ModelForm):
    # title = forms.CharField(label='Title')
    # content = forms.CharField(label='Content')

    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        # fields = ['title', 'content', 'author', 'categories']
        # fields = '__all__'
        # exclude = ['created_at', 'updated_at']


class LoginForm(forms.Form):
    username = forms.CharField(label='Title')
    password = forms.CharField(label='Content', widget=forms.PasswordInput)

    # class Meta:
    #     model = get_user_model()
    #     fields = ['username', 'password']


