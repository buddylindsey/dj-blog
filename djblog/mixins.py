from djblog.models import Category


class CategoryMixin(object):
    def get_context_data(self, **kwargs):
        context = super(CategoryListMixin, self).get_context_data(**kwargs)
        context['category'] = self.get_category()
        return context

    def get_category(self):
        slug = self.kwargs.get('slug', None)

        if slug is not None:
            return Category.objects.get(slug=slug)
        else:
            raise AttributeError("Must use slug for urls")


class CategoryListMixin(object):
    def get_context_data(self, **kwargs):
        context = super(CategoryListMixin, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
