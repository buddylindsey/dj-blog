import mox

from django.http import Http404
from django.test import TestCase
from django.test.client import RequestFactory
from django.views.generic import TemplateView

from model_mommy import mommy

from djblog.models import Category
from djblog.mixins import CategoryMixin, CategoryListMixin, JinjaMixin


class CategoryMixinTest(TestCase):
    class TestView(CategoryMixin, TemplateView):
        pass

    def setUp(self):
        self.view = self.TestView()
        self.view.kwargs = {}
        self.mock = mox.Mox()

    def tearDown(self):
        self.mock.UnsetStubs()

    def test_get_category(self):
        category = mommy.make(Category, name='hello')
        self.view.kwargs['slug'] = 'hello'

        c = self.view.get_category()

        self.assertEqual(c, category)


class CategoryListMixinTest(TestCase):
    class TestView(CategoryListMixin, TemplateView):
        pass

    def setUp(self):
        self.view = self.TestView()
        self.mock = mox.Mox()

    def tearDown(self):
        self.mock.UnsetStubs()

    def test_get_context_data(self):
        self.mock.StubOutWithMock(Category.objects, 'all')
        Category.objects.all().AndReturn('other')

        self.mock.ReplayAll()
        context = self.view.get_context_data()
        self.mock.VerifyAll()

        self.assertEqual(context['categories'], 'other')


class JinjaMixinTest(TestCase):
    class TestView(JinjaMixin, TemplateView):
        template_name = 'djblog/index'

    def setUp(self):
        self.view = self.TestView()

    def test_get_template_names_wo_jinja(self):
        with self.settings(INSTALLED_APPS=('template',)):
            result = self.view.get_template_names()
        self.assertEqual(['djblog/index.html'], result)

    def test_get_template_names_w_jinja(self):
        with self.settings(INSTALLED_APPS=('django_jinja',)):
            result = self.view.get_template_names()
        self.assertEqual(['djblog/index.jinja'], result)
