from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class CheckForm(forms.Form):
    isChecked = forms.BooleanField(required=False)


class addMoneyForm(forms.Form):
    amount = forms.IntegerField(max_value=1000)

class FoodItemForm(forms.Form):
    item = forms.CharField(widget=forms.HiddenInput())
    type = forms.CharField(widget=forms.HiddenInput())
    amount = forms.IntegerField()

class IngredientsForm(forms.Form):
    type = forms.CharField(widget=forms.HiddenInput())
    amount = forms.IntegerField()
