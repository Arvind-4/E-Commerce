from django.urls import re_path

from pages.views import ReactView

reactUrls = [
    re_path(r"^$", ReactView.as_view(), name='react-home'),
    re_path(r"^about/$", ReactView.as_view(), name='react-about'),
    re_path(r"^products/$", ReactView.as_view(), name='react-products'),
    re_path(r"^product/(?P<id>[0-9a-f-]+)/$", ReactView.as_view(), name='react-product'),
    re_path(r"^categories/$", ReactView.as_view(), name='react-categories'),
    re_path(r"^contact-us/$", ReactView.as_view(), name='react-contact-us'),
    re_path(r"^about-us/$", ReactView.as_view(), name='react-about-us'),
    re_path(r"^accounts/$", ReactView.as_view(), name='react-accounts'),
]