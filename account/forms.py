from django.utils.translation import gettext_lazy as _
from .models import validate_image_size
from django.core import validators
from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": _("username")}),
        label=_("username")
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": _("password")}),
        label=_("password")
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": _("username")}),
        label=_("username"),
        validators=[
            validators.MinLengthValidator(8, _("username cannot be less than 8 characters.")),
            validators.MaxLengthValidator(20, _("username cannot be more than 20 characters."))
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": _("password")}),
        label=_("password"),
        validators=[
            validators.MinLengthValidator(8,
                                          _("short passwords are easy to guess. Try one with at least 8 characters."))
        ]
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": _("confirm password")}),
        label=_("confirm password")
    )

    picture = forms.ImageField(
        label=_("picture"),
        validators=[
            validate_image_size,
            validators.FileExtensionValidator(allowed_extensions=("PNG", "JPG", "JPEG"))
        ]
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)

        if qs.exists():
            raise forms.ValidationError(f"{username} already taken.")

        return username

    def clean_password2(self):
        pwd = self.cleaned_data.get("password")
        pwd2 = self.cleaned_data.get("password2")

        if pwd != pwd2:
            raise forms.ValidationError(_("passwords do not match."))

        return pwd
