from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='', max_length=50)