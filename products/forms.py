from django import forms

class PriceFilter(forms.Form):
    min = forms.IntegerField()
    max = forms.IntegerField()