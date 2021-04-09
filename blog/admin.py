from django.contrib import admin
from blog.models import ArticleCategory, Article


# 导入模型类: 注册
@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    # 需要显示的字段
    list_display = ("title", "create")
    # 可以搜索的字段
    search_fields = ("title",)
    # 过滤的字段
    list_filter = search_fields


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 需要显示的字段
    list_display = ("category", "title", "publish_date", "update_date", "total_view")
    # 可以搜索的字段
    search_fields = ("category", "title", "brief_content", "content")
    # 过滤的字段
    list_filter = search_fields


admin.site.site_header = '个人博客后台'
admin.site.site_title = '登陆后台'
admin.site.index_title = '后台管理'
