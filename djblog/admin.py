from django.contrib import admin

from djblog.models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
