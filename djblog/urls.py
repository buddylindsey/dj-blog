from django.conf.urls import patterns, url

from djblog.views import (
    ArticleView, ArticlePreviewView, IndexView, CategoryView)

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', ArticleView.as_view(), name='article'),
    url(
        r'^(?P<slug>[-\w]+)/preview/$', ArticlePreviewView.as_view(),
        name='article_preview'),
    url(
        r'^category/(?P<slug>[-\w]+)/$', CategoryView.as_view(),
        name='category'),
)
