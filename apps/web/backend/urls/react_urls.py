from django.urls import re_path
from django.views.generic import TemplateView

def index(request):
    return TemplateView.as_view(template_name='base.html')(request)

reactUrls = [
    re_path(r"^$", index, name='react-home'),
    re_path(r"^about/$", index, name='react-about'),
    re_path(r"^products/$", index, name='react-products'),
    re_path(r"^categories/$", index, name='react-categories'),
    re_path(r"^contact-us/$", index, name='react-contact-us'),
    re_path(r"^about-us/$", index, name='react-about-us'),
    re_path(r"^accounts/$", index, name='react-accounts'),
]