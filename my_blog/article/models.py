# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


# @python_2_unicode_compatible
# class Author(models.Model):
#     """docstring for Author"""
#     name = models.CharField(max_length=30)
#     email = models.EmailField(blank=True)
#     website = models.URLField(blank=True)

#     def __str__(self):
#         return self.name


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=16, verbose_name='分类名称')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    tag_name = models.CharField(max_length=16, verbose_name='标签名称')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name


@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField('标题', max_length=100)
    # author = models.ForeignKey(Author)
    content = models.TextField('正文', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    publish_time = models.DateTimeField('发布时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_time']


class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='博客')
    name = models.CharField('称呼', max_length=16)
    email = models.EmailField(blank=True)
    content = models.CharField('内容', max_length=140)
    created = models.DateTimeField('发布时间', auto_now_add=True)
