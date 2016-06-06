from django.contrib import admin
from article.models import Category, Tag
from article.models import Blog, Comment

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
	list_display = ('tag_name', 'create_time')


class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'publish_time', 'update_time',)


class CommentAdmin(admin.ModelAdmin):
	list_display = ('blog', 'name', 'email', 'created',) 


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)


