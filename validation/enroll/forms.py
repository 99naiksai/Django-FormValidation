from django import forms
from django.core import validators
def start_with_s(value):
    if value[0]!='s':
        raise forms.ValidationError('name should start with s')
class StudentRegistration(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])#built-in validator
    name1 = forms.CharField(validators=[start_with_s])#custom validator
