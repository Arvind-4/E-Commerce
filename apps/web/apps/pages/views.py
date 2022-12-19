from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import View

# Create your views here.

def handler404(request:HttpRequest, *args, **kwargs):
    return render(request, 'error/404.html', status=404, context={})

def handler500(request:HttpRequest, *args, **kwargs):
    return render(request, 'error/500.html', status=500, context={})

class ReactView(View):
    template_name = "base.html"
    context = {}
    def get(self, request:HttpRequest, *args, **kwargs):
        return render(request, self.template_name, self.context)