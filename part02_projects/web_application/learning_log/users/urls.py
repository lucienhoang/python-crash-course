"""Defines URL patterns for users."""

from django.contrib.auth.views import LoginView
from django.urls import path

from . import views
from .forms import LoginForm

app_name = "users"

urlpatterns = [
    # Login page
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
    # Registration page
    path("register/", views.register, name="register"),
    # Logout page
    path("logout/", views.logout_view, name="logout"),
]
