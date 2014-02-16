from django.conf.urls import patterns, url

from djblog.views import ArticleView, IndexView, CategoryView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='blog_index'),
    url(r'^(?P<slug>[-\w]+)/$', ArticleView.as_view(), name='blog_article'),
    url(
        r'^category/(?P<slug>[-\w]+)/$', CategoryView.as_view(),
        name='blog_category'),
)
