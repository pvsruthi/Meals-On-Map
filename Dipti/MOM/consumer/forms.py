from django import forms

class SearchForm(forms.Form):
    zipcode = forms.CharField(label='ZIPCODE', max_length = 5)
    date = forms.DateField(label='DATE')

