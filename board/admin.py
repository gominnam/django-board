from django.contrib import admin
from board.models import PostCategory, Post


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
