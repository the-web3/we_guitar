#encoding=utf-8


import pytz
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
from common.models import BaseModel
from django.contrib.auth.models import User


tz = pytz.timezone(settings.TIME_ZONE)


class Banner(BaseModel):
    title = models.CharField(max_length=200, default='', verbose_name='标题')
    img = models.ImageField(upload_to='banner/', verbose_name='轮播图')
    url = models.URLField(max_length=100, verbose_name='图片链接')
    active = models.CharField(max_length=250, default='', verbose_name='图片状态')
    is_active = models.BooleanField(default=True, verbose_name='是否是有效')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'

    def as_dict(self):
        return {
            'id': self.id,
            'text_info': self.title,
            'img': str(self.img),
            'link_url': self.url,
            'is_active': self.is_active,
            'uuid': self.uuid,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class Tag(BaseModel):
    name = models.CharField(max_length=100, verbose_name='标签')
    is_active = models.BooleanField(default=True, verbose_name='是否有效')

    class Meta:
        verbose_name = '标签表'
        verbose_name_plural = '标签表'

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'uuid': self.uuid,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class Category(BaseModel):
    name = models.CharField('文章分类', max_length=100)
    icon = models.ImageField(upload_to='cat/%Y/%m/%d/', blank=True, null=True, verbose_name='分类的Icon')
    is_active = models.BooleanField('是否是有效', default=True)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'icon': self.icon,
            'uuid': self.uuid,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class Article(BaseModel):
    title = models.CharField(max_length=70, verbose_name='标题')
    user = models.ForeignKey(
        User, related_name="article_user",
        null=True, blank=True, on_delete=models.CASCADE, verbose_name='作者'
    )
    excerpt = models.TextField(max_length=200, default='', verbose_name='摘要')
    tags = models.ManyToManyField(Tag, blank=True, null=True, verbose_name='标签',)
    category = models.ForeignKey(
        Category, related_name="article_cat",
        on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='分类'
    )
    img = models.ImageField(
        upload_to='article/%Y/%m/%d/', blank=True, null=True, verbose_name='文章图片'
    )
    body = UEditorField(
        width=800, height=500,
        toolbars="full", imagePath="upimg/", filePath="upfile/",
        upload_settings={"imageMaxSize": 1204000},
        settings={}, command=None, blank=True, verbose_name='内容'
    )
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    is_active = models.BooleanField(default=True, verbose_name='是否有效')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    def return_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'excerpt': self.excerpt,
            'img': str(self.img),
            'created_at': self.created_at.astimezone(tz).strftime('%Y-%m-%d %H:%M'),
            'updated_at': self.updated_at.astimezone(tz).strftime('%Y-%m-%d %H:%M')
        }

