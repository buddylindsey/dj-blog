from django.views.generic import ListView, DetailView

from djblog.models import Article
from djblog.mixins import (
    CategoryMixin, CategoryListMixin, JinjaMixin, SuperUserMixin)


class IndexView(JinjaMixin, CategoryListMixin, ListView):
    model = Article
    paginate_by = 10
    context_object_name = 'articles'
    template_name = 'djblog/index'
    queryset = Article.objects.published()


class ArticleView(JinjaMixin, CategoryListMixin, DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'djblog/detail'


class ArticlePreviewView(SuperUserMixin, ArticleView):
    pass


class CategoryView(JinjaMixin, CategoryListMixin, CategoryMixin, ListView):
    model = Article
    paginate_by = 10
    context_object_name = 'articles'
    template_name = 'djblog/category'

    def get_queryset(self):
        return self.get_category().articles.published()
