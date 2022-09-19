import re

from django import forms
from .models import User, GlobalUsers


def allow_digits(phoneno):
    regex = re.compile(r'\d+')
    if not re.match(regex, phoneno):
        raise forms.ValidationError('Phoneno Should Contain digits from 0 to 9')


class UserLoginForm(forms.Form):
    phoneno = forms.CharField(max_length=10, min_length=10, validators=[allow_digits])
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    password = forms.CharField(min_length=8, max_length=50)
    password2 = forms.CharField(min_length=8,max_length=50)
    phoneno = forms.CharField(max_length=10, min_length=10, validators=[allow_digits])

    class Meta:
        model = User
        fields = '__all__'


    def clean(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError("Passwords Doesn't Match")


class GlobalUsersForm(forms.ModelForm):
    class Meta:
        model = GlobalUsers
        fields = '__all__'


class SearchByNameForm(forms.Form):
    name = forms.CharField(max_length=30)


class SearchByNumberForm(forms.Form):
    phoneno = forms.CharField(max_length=10, min_length=10, validators=[allow_digits])


class AddSpamForm(forms.Form):
    phoneno = forms.CharField(max_length=10, min_length=10)
    spam = forms.CharField(min_length=3, widget=forms.CheckboxInput, required=True, validators=[allow_digits])

