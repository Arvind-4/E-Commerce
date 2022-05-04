from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from products.models import Product
from category.models import Category

@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = ('title',)
    settings = {
        'searchableAttributes': ['title',]
    }
    index_name = 'products'


@register(Category)
class CategoryIndex(AlgoliaIndex):
    fields = ('category',)
    settings = {
        'searchableAttributes': ['category',]
    }
    index_name = 'categories'

# python manage.py algolia_reindex: reindex all the registered models. This command will first send all the record to a temporary index and then moves it.
# you can pass --model parameter to reindex a given model
# python manage.py algolia_applysettings: (re)apply the index settings.
# python manage.py algolia_clearindex: clear the index