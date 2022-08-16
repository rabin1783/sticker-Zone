
from dataclasses import fields
from pyexpat import model
from statistics import mode
from django import forms
from animeapps.models import AppUser

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ('email','password')

        model = AppUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:

        fields = ('first_name','middle_name','last_name',\
                'email','password','contact','dob','address')
        
        model = AppUser

class OtpForm(forms.ModelForm):
    class Meta:
        fields = ('verification_code',)

        model = AppUser
            





