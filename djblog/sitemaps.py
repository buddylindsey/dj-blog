from django.contrib.sitemaps import Sitemap

from djblog.models import Article


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = "https"

    def items(self):
        return Article.objects.published()
