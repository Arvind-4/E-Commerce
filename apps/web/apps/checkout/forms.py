from django import forms
from django.contrib.auth import get_user_model

from .models import Checkout

User = get_user_model()

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = [
            'name',
            'email',
            'address',
            'city',
            'state',
            'number',
            'zip_code',
            'country',
        ]

    def __init__(self, *args, **kwargs):
        super(CheckOutForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'focus:outline-none px-3 w-full'
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        qs_email = User.objects.filter(email__iexact=email)
        if not qs_email.exists():
            raise forms.ValidationError(
                "This email is not Registered. Please Register to continue."
            )
        return email