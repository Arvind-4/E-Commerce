from django.shortcuts import render

# Create your views here.

def error_404(request, exception=404):
    return render(request,'error/404.html', context={})

def error_500(request,  exception):
        context = {}
        return render(request,'error/500.html', context=context)