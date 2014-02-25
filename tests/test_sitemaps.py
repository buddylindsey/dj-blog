from django.test import TestCase

from model_mommy import mommy

from djblog.models import Article
from djblog.sitemaps import ArticleSitemap


class ArticleSitemapTest(TestCase):
    def setUp(self):
        self.sitemap = ArticleSitemap()

    def test_attrs(self):
        self.assertEqual(self.sitemap.changefreq, 'daily')
        self.assertEqual(self.sitemap.priority, 0.5)
        self.assertEqual(self.sitemap.protocol, 'https')

    def test_items(self):
        mommy.make('djblog.Article', status=1)
        mommy.make('djblog.Article', status=0, _quantity=2)

        self.assertEqual(Article.objects.published().count(), 1)
