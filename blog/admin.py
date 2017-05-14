# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *

# Register your models here.
# @admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'click_count',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'content',)
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend', 'user', 'category', 'tag',)
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh-CN.js',
            '/static/js/kindeditor/config.js'
        )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)