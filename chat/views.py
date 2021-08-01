from django.shortcuts import render


# Create your views here.

def room_page(request, *args, **kwargs):
    room_name = kwargs.get("room_name")

    context = {
        "room_name": room_name
    }

    return render(request, "room.html", context)
