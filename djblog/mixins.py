from django.http import Http404

from djblog.models import Category


class CategoryMixin(object):
    def get_context_data(self, **kwargs):
        context = super(CategoryMixin, self).get_context_data(**kwargs)
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


class SuperUserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise Http404

        return super(SuperUserMixin, self).dispatch(request, *args, **kwargs)
