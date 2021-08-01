from django.contrib import admin
from .forms import GroupForm
from .models import Group


# Register your models here.


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    form = GroupForm
    list_display = ("__str__", "date", "active")
    list_editable = ("active",)

    class Meta:
        model = Group
