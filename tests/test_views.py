from django.test import TestCase

import mox

from djblog.views import IndexView, ArticleView, CategoryView
from djblog.models import Article


class IndexViewTest(TestCase):
    def setUp(self):
        self.view = IndexView()

    def test_attrs(self):
        self.assertEqual(self.view.model, Article)
        self.assertEqual(self.view.context_object_name, 'articles')
        self.assertEqual(self.view.template_name, 'djblog/index.html')


class ArticleViewTest(TestCase):
    def setUp(self):
        self.view = ArticleView()

    def test_attrs(self):
        self.assertEqual(self.view.model, Article)
        self.assertEqual(self.view.context_object_name, 'article')
        self.assertEqual(self.view.template_name, 'djblog/detail.html')


class CategoryViewTest(TestCase):
    def setUp(self):
        self.view = CategoryView()
        self.view.object_list = {}
        self.view.object = object
        self.view.kwargs = {}
        self.mock = mox.Mox()

    def tearDown(self):
        self.mock.UnsetStubs()

    def test_attrs(self):
        self.assertEqual(self.view.model, Article)
        self.assertEqual(self.view.context_object_name, 'articles')
        self.assertEqual(self.view.template_name, 'djblog/category.html')
