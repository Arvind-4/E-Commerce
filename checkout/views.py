from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import CheckOutForm
from carts.models import Cart

@login_required
def checkout_view(request):
    qs_cart = Cart.objects.filter(user=request.user)
    email = request.user.email
    form = CheckOutForm(request.POST or None, initial={
        'email': email
    })
    if not qs_cart.exists():
        raise Http404
    context = {
        'object': qs_cart.first(),
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'checkout/checkout.html', context=context)