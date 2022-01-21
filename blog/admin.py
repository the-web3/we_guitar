#encoding=utf-8

from django.contrib import admin
from blog.models import (
    Banner, Category, Article, Tag
)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'img', 'url', 'is_active'
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'views', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'title')