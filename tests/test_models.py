import mox

from django.test import TestCase

from mistune import Markdown
from model_mommy import mommy

from djblog.models import Article


class ArticleTest(TestCase):
    def setUp(self):
        self.mock = mox.Mox()

    def tearDown(self):
        self.mock.UnsetStubs()

    def test_is_published(self):
        article = mommy.make('djblog.Article', status=1)

        self.assertTrue(article.is_published())

    def test_is_not_published(self):
        article = mommy.make('djblog.Article', status=0)

        self.assertFalse(article.is_published())

    def test_get_absolute_url(self):
        article = mommy.make('djblog.Article', title='i win')
        self.assertEqual('/test/i-win/', article.get_absolute_url())

    def test_published_body(self):
        article = mommy.make('djblog.Article', body='hello')

        self.mock.StubOutWithMock(Markdown, 'render')
        Markdown.render('hello').AndReturn('converted text')

        self.mock.ReplayAll()
        a = article.published_body()
        self.mock.VerifyAll()

        self.assertEqual(a, 'converted text')


class ArticleManagerTest(TestCase):
    def setUp(self):
        mommy.make('djblog.Article', status=0)
        mommy.make('djblog.Article', status=1, _quantity=2)

    def test_get_published(self):
        self.assertEqual(2, Article.objects.published().count())
