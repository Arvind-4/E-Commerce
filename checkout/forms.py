from django import forms
from django_countries import countries
from django.core.validators import RegexValidator

COUNTRY_CHOICES = tuple(countries)

class CheckOutForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=400, required=True)
    city = forms.CharField(max_length=225, required=True)
    state = forms.CharField(max_length=225, required=True)
    number = forms.IntegerField(required=True)
    zip = forms.CharField(max_length=10, required=True)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=True)

    def __init__(self, *args, **kwargs):
        # print('The request', self.request)
        super(CheckOutForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'focus:outline-none px-3 w-full'