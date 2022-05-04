from backend.django_algolia.client import get_index

# def perform_search(query):
#     index = get_index()
#     params = {
#         'hitsPerPage': 10
#     }
#     results = index.search(query, params)
#     return results

def search_index(query):
    index = get_index()
    return index.search(query)