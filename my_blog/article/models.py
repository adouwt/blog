# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User, UserManager


@python_2_unicode_compatible
class Category(models.Model):
    """ 类别 """
    name = models.CharField(max_length=16, verbose_name='类别名称')
    parent = models.ForeignKey('self', default=None, blank=True, null=True,
                               verbose_name=u'上级分类')
    rank = models.IntegerField(default=0, verbose_name=u'排序')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'分类'
        ordering = ['rank', '-create_time']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    """ 标签 """
    tag_name = models.CharField(max_length=16, verbose_name='标签名称')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = u'标签'

    def __str__(self):
        return self.tag_name


@python_2_unicode_compatible
class Blog(models.Model):
    """ 博客 """
    title = models.CharField('标题', max_length=100)
    img = models.CharField(max_length=200, verbose_name='图片')
    # default='/static/img/article/default.jpg', 
    view_num = models.IntegerField(default=0, verbose_name='浏览量')
    like_num = models.IntegerField(default=0, verbose_name='点赞数')
    comment_num = models.IntegerField(default=0, verbose_name='评论数')
    author = models.ForeignKey(User, verbose_name='作者')
    summary = models.TextField(verbose_name=u'摘要')
    content = models.TextField('正文', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    publish_time = models.DateTimeField('发布时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    is_recommend = models.BooleanField(default=False, verbose_name='是否被推荐')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = u'博客文章'
        ordering = ['-publish_time']


@python_2_unicode_compatible
class Comment(models.Model):
    """ 评论 """
    blog = models.ForeignKey(Blog, verbose_name='博客')
    comment_user = models.ForeignKey(User, verbose_name='评论用户')
    content = models.TextField('评论内容', max_length=140)
    create_time = models.DateTimeField('发布时间', auto_now_add=True)
    parent = models.ForeignKey('self', default=None, blank=True, null=True,
                               verbose_name=u'引用')

    class Meta:
        verbose_name = verbose_name_plural = '评论'
        ordering = ['-create_time']

    def __str__(self):
        return self.blog


# @python_2_unicode_compatible
# class LikeBlog(models.Model):
#     """docstring for LikeGame"""
#     like_blog = models.ForeignKey(Blog, verbose_name='博客')
#     like_user = models.ForeignKey(User, verbose_name='点赞人')
#     like_date = models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')

#     class Meta:
#         verbose_name = "点赞"
#         verbose_name_plural = "点赞"

#     def __str__(self):
#         return self.like_user


# 向User表中添加字段扩充User
from django.contrib.auth.admin import UserAdmin  
class ProfileBase(type):  
    def __new__(cls, name, bases, attrs):  
        module = attrs.pop('__module__')  
        parents = [b for b in bases if isinstance(b, ProfileBase)]  
        if parents:  
            fields = []  
            for obj_name, obj in attrs.items():  
                if isinstance(obj, models.Field): fields.append(obj_name)  
                User.add_to_class(obj_name, obj)  
            UserAdmin.fieldsets = list(UserAdmin.fieldsets)  
            UserAdmin.fieldsets.append((name, {'fields': fields}))  
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)  

          
class Profile(object):  
    __metaclass__ = ProfileBase  

 
# 如果后来想添加字段,可以在这后面加 
class MyProfile(Profile): 
    headImage = models.ImageField(upload_to='/static/image/users/', default='/static/image/users/default.jpg', blank=True)
    integral = models.IntegerField(default=0, verbose_name='积分')
    is_recommend = models.BooleanField(default=False, verbose_name='是否被推荐')