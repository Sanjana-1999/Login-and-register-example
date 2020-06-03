from django import forms
from proapp.models import UserInfoModel
from django.contrib.auth.models import User

class UserInfo(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')

class profileInfo(forms.ModelForm):
    class Meta():
        model=UserInfoModel
        fields=('portfolio_site','profile_pic')
