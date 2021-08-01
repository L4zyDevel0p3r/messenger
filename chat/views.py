from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required(login_url="/login")
def room_page(request, *args, **kwargs):
    room_name = kwargs.get("room_name")

    context = {
        "room_name": room_name
    }

    return render(request, "room.html", context)
