from django.urls import path

from .views import (
    signin_view,
    signup_view,
    signout_view,
)

from .views import (
    ResetPasswordView,  
    PasswordResetDoneView,
    CustomChangePassword
)

from .forms import PasswordResetConfirmForm

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign-in/', signin_view, name='sign-in'),
    path('sign-up/', signup_view, name='sign-up'),
    path('sign-out/', signout_view, name='sign-out'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        form_class=PasswordResetConfirmForm,
        template_name='accounts/password-reset/password-reset-confirm.html'
    ),
    name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password-reset/password-reset-complete.html'
        ),
         name='password_reset_complete'),

    path('change-password/', CustomChangePassword.as_view(), name='change-password'),
]