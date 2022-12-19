from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

from .forms import CheckOutForm
from .models import Checkout
from carts.models import Cart


@login_required
def checkout_view(request):
    qs_cart = Cart.objects.filter(user=request.user)
    initial_data = {}
    email = request.user.email
    initial_data['email'] = email
    # qs_checkout = Checkout.objects.filter(user=request.user)
    # if qs_checkout.exists():
    #     obj = qs_checkout.first()
    #     if obj.remember_me:
    #         initial_data = obj.__dict__

    form = CheckOutForm(request.POST or None, initial={"email": request.user.email})
    if not qs_cart.exists():
        raise Http404
    context = {
        'object': qs_cart.first(),
        'form': form,
    }
    if form.is_valid():
        user = form.save(commit=False)
        user.user = request.user
        user.email = request.user.email
        user.save()
        messages.success(request, 'Your order has been placed successfully.')
        # subject = '''Order Details from E-Commerce'''
        # body = 'Your Order has been Successfully Placed!'
        # email = EmailMessage(
        #     subject=subject,
        #     body=body,
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     reply_to=[request.user.email,]
        # )
        # # sent = email.send(fail_silently=False)
        # sent = email.send()
        # print('The sent is ', sent)
        # if sent:
        #     return redirect('checkout-success')
        # else:
        #     raise Http404
        return redirect('checkout-success')
    return render(request, 'checkout/checkout.html', context=context)


def checkout_success_view(request):
    return render(request, 'checkout/success.html')