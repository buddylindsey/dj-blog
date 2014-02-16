from django.views.generic import ListView, DetailView

from djblog.models import Article
from djblog.mixins import CategoryMixin, CategoryListMixin


class IndexView(CategoryListMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'djblog/index.html'
    queryset = Article.objects.published()


class ArticleView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'djblog/detail.html'


class CategoryView(CategoryMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'djblog/category.html'
