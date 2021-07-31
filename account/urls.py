from .views import login_page, logout_view
from django.urls import path

app_name = "Account"

urlpatterns = [
    path('login', login_page, name="Login"),
    path('logout', logout_view, name="Logout"),
]
