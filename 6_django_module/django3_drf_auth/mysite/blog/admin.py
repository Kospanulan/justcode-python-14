from django.contrib import admin

from blog.models import Category, Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'title', 'content', 'author', 'created_at']
    list_editable = ['title', 'author']
    list_per_page = 3
    list_filter = ['author']
    search_fields = ['title', 'content']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
