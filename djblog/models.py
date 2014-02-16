from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from markdown2 import Markdown

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

DRAFT = 0
PUBLISHED = 1


class ArticleQueryset(models.query.QuerySet):
    def published(self):
        return self.filter(status=PUBLISHED)


class ArticleManager(models.Manager):
    def get_query_set(self):
        return ArticleQueryset(self.model, using=self._db)

    def published(self):
        return self.get_query_set().published()


@python_2_unicode_compatible
class Article(TimeStampedModel):
    title = models.CharField(
        _('title'), max_length=255,
        help_text=_('A unique title for a blog post.'), unique=True)
    publish_date = models.DateTimeField(
        blank=True, null=True,
        help_text=_('The date that you published the blog post.'))

    body = models.TextField(
        blank=True, help_text=_(('Text for the body of your blog post.'
                                 'Should be in markdown')))

    slug = AutoSlugField(_('slug'), populate_from='title')

    STATUS_CHOICES = ((DRAFT, _('draft')), (PUBLISHED, _('published')))
    status = models.IntegerField(
        _('status'), choices=STATUS_CHOICES, default=DRAFT)

    objects = ArticleManager()

    def is_published(self):
        return self.status == PUBLISHED

    def get_absolute_url(self):
        return reverse('blog_article', kwargs={'slug': self.slug})

    def published_body(self):
        md = Markdown()
        return md.convert(self.body)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(_('slug'), populate_from='name')
    articles = models.ManyToManyField(Article, related_name='categories')

    def __str__(self):
        return self.name
