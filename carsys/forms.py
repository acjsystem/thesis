from django import forms
from django.contrib.auth.models import User
#from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

 #ASK Suinan if you can make your own User model and how it works
