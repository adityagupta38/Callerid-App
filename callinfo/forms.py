import re

from django import forms
from .models import User, GlobalUsers


class UserLoginForm(forms.Form):
    phoneno = forms.CharField(max_length=10, min_length=10)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    password2 = forms.CharField(max_length=50)
    phoneno = forms.CharField(max_length=10, min_length=10)

    class Meta:
        model = User
        fields = '__all__'

    def clean_phoneno(self):
        phoneno = self.cleaned_data.get('phoneno')
        regex = re.compile(r'\d+')
        if re.match(regex, phoneno):
            return phoneno
        else:
            raise forms.ValidationError('Phoneno Should Contain digits from 0 to 9')

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
    phoneno = forms.IntegerField()
