# -*- coding:utf-8 -*-
from article.models import Category, Tag
from article.models import Blog, Comment
from article.models import LikeBlog

def get_comment_num(field):
	num = Comment.objects.filter()