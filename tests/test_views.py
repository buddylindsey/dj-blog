from django.test import TestCase

from model_mommy import mommy

import mox

from djblog.views import IndexView, ArticleView, CategoryView
from djblog.models import Article


class IndexViewTest(TestCase):
    def setUp(self):
        self.view = IndexView()

    def test_attrs(self):
        self.assertEqual(self.view.model, Article)
        self.assertEqual(self.view.context_object_name, 'articles')
        self.assertEqual(self.view.template_name, 'djblog/index')


class ArticleViewTest(TestCase):
    def setUp(self):
        self.view = ArticleView()

    def test_attrs(self):
        self.assertEqual(self.view.model, Article)
        self.assertEqual(self.view.context_object_name, 'article')
        self.assertEqual(self.view.template_name, 'djblog/detail')


class CategoryViewTest(TestCase):
    def setUp(self):
        self.view = CategoryView()
        self.mock = mox.Mox()

    def tearDown(self):
        self.mock.UnsetStubs()

    def test_attrs(self):
        self.assertEqual(self.view.model, Article)
        self.assertEqual(self.view.context_object_name, 'articles')
        self.assertEqual(self.view.template_name, 'djblog/category')

    def test_get_queryset(self):
        article1, article2 = mommy.make(
            'djblog.Article', status=Article.PUBLISHED, _quantity=2)
        article3 = mommy.make('djblog.Article')
        cat = mommy.make('djblog.Category')
        cat.articles.add(article1)
        cat.articles.add(article2)
        cat.articles.add(article3)

        self.mock.StubOutWithMock(self.view, 'get_category')
        self.view.get_category().AndReturn(cat)

        self.mock.ReplayAll()
        qs = self.view.get_queryset()
        self.mock.VerifyAll()

        self.assertSequenceEqual([article1, article2], qs)

