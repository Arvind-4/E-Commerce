from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect
)
from .forms import (
    SignInForm,
    SignUpForm
)


def signup_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        print('The Cleaned Dsta is ', form.cleaned_data)
        user = form.save(commit=False)
        
            # email    = form.cleaned_data.get('email')
            # raw_pass = form.cleaned_data.get('password1')
            # account = authenticate(email=email, password = raw_pass)
            # login(request, account)
            # messages.success(request, "You have been Registered as {}".format(request.user.username))
        return redirect('sign-in')
    context = {
        'form': form,
    }
    return render(request, 'accounts/sign-up.html', context)


def signin_view(request):
    form = SignInForm(request.POST or None)
    if form.is_valid():
        email   = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user =  authenticate(email=email, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next') or None
            if next_url:
                return redirect(next_url)
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'accounts/sign-in.html', context)

@login_required
def signout_view(request):
    print(request.user.is_authenticated)
    logout(request)
    return redirect('/')