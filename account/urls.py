from .views import login_page
from django.urls import path

app_name = "Account"

urlpatterns = [
    path('login', login_page, name="Login"),
]
