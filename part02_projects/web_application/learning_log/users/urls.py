"""Defines URL patterns for users."""

from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    # Login page
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    # Logout page
    path("logout/", views.logout_view, name="logout"),
]
