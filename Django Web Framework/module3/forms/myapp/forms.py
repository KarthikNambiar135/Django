from django import forms
from django.forms.widgets import NumberInput

EXAMPLE = [
    ('italian', 'Italian'),
    ('greek', 'Greek'),
    ('indian', 'Indian')
]


class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs = {'rows':5}))
    email = forms.EmailField(label="Enter a Email address")
    res_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    cuisine = forms.ChoiceField(widget=forms.RadioSelect, choices=EXAMPLE)