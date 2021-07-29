"""
forms file
"""
from django import forms


class DownloadProjectForm(forms.Form):
    """ used to validate the input from the user """

    project_name = forms.CharField(max_length=30)
    auth_type = forms.ChoiceField(choices=(('auth', 'auth'), ('jwt', 'jwt')))
    notification = forms.BooleanField(required=False)
