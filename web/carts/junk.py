# token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]

# valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
# print(valid_data.keys())
# user_id = valid_data.get('user_id')
# access_token = AccessToken(token)


# user = User.objects.get(id=access_token['user_id'])
# print('The User Data is ',self.request)
# print(user_frontent)
# self.request.user = user_id

# print(Cart.products.objects.all())
# print(product_obj.slug)      
# print(qs)  
# id_ = int(user_id)
# qs_user = User.objects.get(user=self.request.user)
# print(qs_user)
# print(self.request.META.keys())
# print(self.kwargs)
# print(qs_cart)   
#     def new_or_get(self, request):
#         # cart_id = request.session.get("cart_id", None)
#         valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
#         # print(valid_data.keys())
#         user_frontent = valid_data.get('user_id')
#         print(user_frontent)
#         self.request.user = user_frontent
#         qs = self.get_queryset().filter(user__id=user_frontent)
#         if qs.exists():
#             new_obj = False
#             cart_obj = qs.first()
#             # if request.user.is_authenticated() and cart_obj.user is None:
#             cart_obj.user.id = user_frontent
#             cart_obj.save()
#         else:
#             cart_obj = Cart.objects.new(user__id=user_frontent)
#             new_obj = True
#             # request.session['cart_id'] = cart_obj.id
#         return cart_obj, new_obj