from django.views.generic import ListView, DetailView

from djblog.models import Article
from djblog.mixins import CategoryMixin, CategoryListMixin, SuperUserMixin


class IndexView(CategoryListMixin, ListView):
    model = Article
    paginate_by = 10
    context_object_name = 'articles'
    template_name = 'djblog/index.html'
    queryset = Article.objects.published()


class ArticleView(CategoryListMixin, DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'djblog/detail.html'


class ArticlePreviewView(SuperUserMixin, ArticleView):
    pass


class CategoryView(CategoryListMixin, CategoryMixin, ListView):
    model = Article
    paginate_by = 10
    context_object_name = 'articles'
    template_name = 'djblog/category.html'
