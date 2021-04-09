from django.views import View
from blog.models import ArticleCategory,Article
from django.http import HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
import markdown


class IndexView(View):
    """
    首页
    """

    @staticmethod
    def get(request):
        """
        首页数
        据
        :return:
        """
        cat_id = request.GET.get('cat_id', 1)
        page_num = request.GET.get('page_num', 1)
        page_size = request.GET.get('page_size', 10)

        # 判断分类id
        try:
            category = ArticleCategory.objects.get(id=cat_id)
        except ArticleCategory.DoesNotExist:
            return HttpResponseNotFound("没有此分类")

        # 获取博客的分类信息
        categories = ArticleCategory.objects.all()

        # 分页数据
        articles = Article.objects.filter(
            category=category
        )

        # 创建分页器
        paginator = Paginator(articles, per_page=page_size)
        # 获取每页的数据
        try:
            page_article = paginator.page(page_num)
        except EmptyPage:
            # 如果没有分页数据
            return HttpResponseNotFound('404 page')

        # 获取列表总页数
        total_page = paginator.num_pages
        context = {
            'categories': categories,
            'category': category,
            'articles': page_article,
            'page_size': page_size,
            'total_page': total_page,
            'page_num': page_num,
        }
        print(articles[0].publish_date)
        return render(request, 'blog/index.html', context=context)


class DetailView(View):
    """
    文章详情
    """

    @staticmethod
    def get(request):
        """
        :param request:
        :return:
        """
        aid = request.GET.get('id')
        page_num = request.GET.get('page_num', 1)
        page_size = request.GET.get('page_size', 5)
        categories = ArticleCategory.objects.all()
        try:
            article = Article.objects.get(article_id=aid)
        except Article.DoesNotExist:
            return render(request, '404.html')
        else:
            # 每次访问都给文章的浏览量加1
            article.total_view += 1
            article.save()

        # 根据之前的浏览数设置推荐文章: 推荐那些浏览量高的文章
        hot_articles = Article.objects.order_by('-total_view')[:9]
        context = {
            'categories': categories,
            'category': article.category,
            'article': article,
            'hot_articles': hot_articles,
            'page_size': page_size,
            'page_num': page_num,
        }
        # 记得在顶部引入 markdown 模块
        context['article'].content = markdown.markdown(context['article'].content, extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        print(context)
        return render(request, 'blog/detail.html', context=context)



