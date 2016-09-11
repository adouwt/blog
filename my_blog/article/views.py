# -*- coding:utf-8 -*-
from django.shortcuts import render
from article.models import Category, Tag
from article.models import Blog, Comment


# 返回部分最近发布的博客
def blog_list(request):
	start = int(request.GET.get("start", 0))
    end = int(request.GET.get("end", 10))
    blogs = Blog.objects.all()[start:end]
    # 将数据库获得的数据转化成json格式的数据
    js_blogs = []
    for one_blog in blogs:
        obj = model_to_dict(one_blog)
        js_blogs.append(obj)
    return JsonResponse(js_blogs, safe=False)


# 获得评论最多的博客5条
def hot_blogs(request):
	blogs = Blog.objects.order_by('-comment_num')[0:5]
    js_blogs = []
    for one_blog in blogs:
        obj = model_to_dict(one_blog)
        js_blogs.append(obj)
    return JsonResponse(js_blogs, safe=False)