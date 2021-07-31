from django.utils.translation import gettext_lazy as _
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": _("username")}),
        label=_("username")
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": _("password")}),
        label=_("password")
    )
