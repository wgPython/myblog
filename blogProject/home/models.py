#!/usr/bin/python3
# -*-coding:utf8-*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django_markdown.models import MarkdownField
from tinymce.models import HTMLField


class Category(models.Model):
    """
    分类名
    """
    name = models.CharField(max_length=100, verbose_name='分类')

    def __str__(self):
        # 返回类名
        return self.name

    class Meta:
        # 元类
        db_table = "Category"
        verbose_name = "分类"
        verbose_name_plural = "分类s"


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=100, verbose_name='标签')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Tag"
        verbose_name = "标签"
        verbose_name_plural = "标签s"


class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=100, verbose_name='标题')
    # 文章简介   blank=True 表示可以不写 没有的话　　此字段必须要有值
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='简介')

    content = models.TextField(verbose_name='内容')
    # 富文本
    # content = HTMLField(verbose_name='内容')
    # content = MarkdownField()

    create_time = models.DateTimeField(verbose_name='建立时间')
    modified_time = models.DateTimeField(verbose_name='修改时间')  # 修改时间
    # 分类外键
    category = models.ForeignKey(Category, verbose_name='分类')
    # 多对多　文章和标签
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')

    # 作者 一对多关系一篇文章只有一个作者
    # author = models.ForeignKey(User)

    on_click = models.IntegerField(default=0, verbose_name='点击量')

    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('home:details', kwargs={'pk': self.pk})

    # 元类
    class Meta:
        db_table = "Article"
        verbose_name = "文章"
        verbose_name_plural = "文章s"
