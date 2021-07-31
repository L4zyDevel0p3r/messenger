from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm


# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")

    login_form = LoginForm(request.POST or None)

    context = {
        "login_form": login_form
    }

    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            context["login_form"] = LoginForm()
            return redirect("/")
        else:
            login_form.add_error("password", _("Incorrect username or password."))

    return render(request, "auth/login.html", context)
