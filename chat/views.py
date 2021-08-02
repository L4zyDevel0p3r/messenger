from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404
from group.models import Group


# Create your views here.

@login_required(login_url="/login")
def room_page(request, *args, **kwargs):
    room_name = kwargs.get("room_name")
    qs = Group.objects.filter(url_name__iexact=room_name, active=True)

    if not qs.exists():
        raise Http404(f"{room_name} not found!")

    context = {
        "room_name": room_name
    }

    return render(request, "room.html", context)
