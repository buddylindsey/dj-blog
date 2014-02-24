from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    '',
    url(r'^test/', include('djblog.urls', namespace='djblog')),
)
