"""
login forms
"""
from django import forms


class LoginForm(forms.Form):
    """ used in admin-login """
    email = forms.EmailField()
    password = forms.CharField(max_length=30)


class ForgotPasswordForm(forms.Form):
    """ used in ForgotPassword """
    email = forms.EmailField()
