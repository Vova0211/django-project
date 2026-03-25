from django import forms

class CreateCardForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50, required=True)
    body = forms.CharField(label='Body', required=True)
    price = forms.FloatField(label='Price', required=True)