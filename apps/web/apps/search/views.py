from django.http import JsonResponse
# from django.conf import settings
# from .client import perform_search

# from .client import search_index

# Create your views here.

# def product_search(request):
#     query = request.GET.get('q') or False
#     print('The query is: ', query)
#     if query:
#         results = search_index(query)
#         print('The results are: ', results)
#         return JsonResponse(results)
#     else:
#         return JsonResponse({})