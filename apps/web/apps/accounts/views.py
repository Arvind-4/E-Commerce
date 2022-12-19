from cgitb import reset
from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
    update_session_auth_hash
)
from django.shortcuts import (
    render,
    redirect
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView

from .forms import (
    SignInForm,
    SignUpForm,
    ForgotPasswordForm,
    ChangeUserPassword,
)

User = get_user_model()

SESSION_EXPIRE_TIME = 604800

def signup_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        print('The Cleaned Dsta is ', form.cleaned_data)
        user = form.save(commit=False)
        email = form.cleaned_data.get('email')
        password =  form.cleaned_data.get('password2')
        user.email = email
        user.set_password(password)
        user.save()
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
        remember_me = request.POST.get('remember_me') or None
        if remember_me is not None:
            request.session.set_expiry(SESSION_EXPIRE_TIME)
            print('You are Remembered!')
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

class ResetPasswordView(PasswordResetView):
    template_name = 'accounts/password-reset/password-reset.html'
    email_template_name = 'accounts/password-reset/email/password-reset-email.html'
    subject_template_name = 'accounts/password-reset/email/password-reset-subject'
    success_url = reverse_lazy('password_reset_done')

    form_class = ForgotPasswordForm

class PasswordResetDoneView(TemplateView):
    template_name = 'accounts/password-reset/password-reset-done.html'

class CustomChangePassword(LoginRequiredMixin, View):
    context = {}
    template_name = 'accounts/change-password/change-password.html'
    def get(self, request, *args, **kwargs):
        form = ChangeUserPassword(request.user)
        self.context['form'] = form
        return render(request, self.template_name, context=self.context)
    def post(self, request, *args, **kwargs):
        form = ChangeUserPassword(request.user, request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save(commit=False)
            password = form.cleaned_data.get('new_password2')
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('/')
        return render(request, self.template_name, context=self.context)