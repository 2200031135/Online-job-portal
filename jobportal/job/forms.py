from django import forms
from .models import Userregistration
from .models import applylogin

class UserRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Userregistration
        field = "all"
        exclude = ["id"]


class applylogin(forms.ModelForm):
    username = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = applylogin
        field = "all"
        exclude = ["id"]




