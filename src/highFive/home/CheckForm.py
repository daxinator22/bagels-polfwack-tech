from django import forms


class CheckForm(forms.Form):
    isChecked = forms.BooleanField()

