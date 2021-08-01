from django.utils.translation import gettext_lazy as _
from .models import Group
from django import forms


class GroupForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data.get("name")
        qs = Group.objects.get_by_name(name)

        if qs is not None and qs != self.instance:
            raise forms.ValidationError(_("This name already exists."))

        return name

    def clean_url_name(self):
        url_name = self.cleaned_data.get("url_name")
        qs = Group.objects.get_by_url_name(url_name)

        if qs is not None and qs != self.instance:
            raise forms.ValidationError(_("This url name already exists."))

        return url_name
