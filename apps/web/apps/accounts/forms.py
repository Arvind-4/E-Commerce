from dataclasses import fields
from django import forms
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordResetForm,
    PasswordChangeForm,
    SetPasswordForm,
)

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=30, help_text = 'Required. Add a valid E-mail address.')
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_email(self, *args, **kwargs):
        form_email = self.cleaned_data.get('email')
        qs_email = User.objects.filter(email=form_email)
        if qs_email.exists() and qs_email.count() == 1:
            information = "The User with the Email is Already Registered! Try Signing In."
            raise forms.ValidationError(information)
        return form_email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            information = "The Passwords didn't Match! Try Again."
            raise forms.ValidationError(information)
        return password2

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-red-200 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full'


class SignInForm(forms.Form):
    email = forms.EmailField(max_length=30, help_text = 'Required. Add a valid E-mail address.')
    password  = forms.CharField(label= 'Password', widget=forms.PasswordInput)

    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid Username or Password!')
        return password

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-red-200 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full'


class ForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(required=True)

    def clean_email(self, *args, **kwargs):
        form_email = self.cleaned_data.get('email') or None
        if form_email is None:
            information1 = 'Email is Required!'
            raise forms.ValidationError(information1)
        qs = User.objects.filter(email=form_email)
        if not qs.exists() and qs.count != 1:
            information2 = "The Entered Email does'nt have an Account! Please Sign Up for a Free Account."
            raise forms.ValidationError(information2)
        return form_email
    def __init__(self, *args, **kwargs):
        super(ForgotPasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent'

class PasswordResetConfirmForm(SetPasswordForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 != password2:
            information = "The Passwords didn't Match! Try Again."
            raise forms.ValidationError(information)
        return password2

    def __init__(self, *args, **kwargs):
        super(PasswordResetConfirmForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent'


class ChangeUserPassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = "__all__"

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 != password2:
            information = "The Passwords didn't Match! Try Again."
            raise forms.ValidationError(information)
        return password2
    
    def __init__(self, *args, **kwargs):
        super(ChangeUserPassword, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'