from django.shortcuts import render
from group.models import Group


# Create your views here.

def home_page(request):
    groups = Group.objects.filter_by_active().order_by("name")

    context = {
        "groups": groups
    }

    return render(request, "home.html", context)


def header(request, *args, **kwargs):
    context = {
        "reqpath": kwargs.get("reqpath")
    }

    return render(request, "shared/header.html", context)
