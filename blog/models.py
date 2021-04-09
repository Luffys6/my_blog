from django.db import models
from mdeditor.fields import MDTextField


class ArticleCategory(models.Model):
    """
    文章分类
    """
    title = models.CharField(max_length=100, help_text="分类名字", verbose_name="分类名字")
    create = models.DateTimeField(auto_now_add=True, help_text="创建时间", verbose_name="创建时间")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name


class Article(models.Model):
    """
    文章
    """
    # 文章分类是一对多   外键：一个栏目对应多个文章
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.CASCADE,
        related_name='article',
        verbose_name='文章类别'
    )
    # 文章的唯一ID
    article_id = models.AutoField(primary_key=True)
    # 文章的标题
    title = models.TextField(verbose_name='文章标题')
    # 文章的摘要
    brief_content = models.TextField(verbose_name='文章摘要')
    # 文章的主要内容
    content = MDTextField(verbose_name='文章内容')
    # 文章的发布时间
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    # 文章更新时间
    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    # 浏览量
    total_view = models.PositiveIntegerField(default=0, verbose_name='浏览量')

    class Meta:
        ordering = ('-publish_date',)
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title




