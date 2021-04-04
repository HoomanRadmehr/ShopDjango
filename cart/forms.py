from django import forms

class AddCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1 , label= 'Qauntity ' )