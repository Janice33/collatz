from django import forms


class MyForm(forms.Form):
    fname= forms.CharField(max_length=100, required=True, label='fname')
    fno= forms.CharField(max_length= 100, label='fno')