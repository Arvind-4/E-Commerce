# from algoliasearch_django import algolia_engine
from algoliasearch.search_client import SearchClient
from django.conf import settings

ALGOLIA_APPLICATION_ID = settings.ALGOLIA.get('APPLICATION_ID')
ALGOLIA_API_KEY = settings.ALGOLIA.get('API_KEY')

def get_index():
    client = SearchClient.create(
        ALGOLIA_APPLICATION_ID, 
        ALGOLIA_API_KEY,
    )
    index = client.init_index('products')
    return index

def initialize_algolia():
    print('initialize_algolia')
    get_index()

# def get_client():
#     return algolia_engine.client

# def get_index(index_name='products'):
#     client = get_client()
#     index = client.init_index(index_name)
#     return index