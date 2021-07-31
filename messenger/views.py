from django.shortcuts import render


# Create your views here.

def home_page(request):
    context = {
    }

    return render(request, "home.html", context)


def header(request, *args, **kwargs):
    context = {
        "reqpath": kwargs.get("reqpath")
    }

    return render(request, "shared/header.html", context)
