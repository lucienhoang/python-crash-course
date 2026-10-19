from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import RegisterForm


# Create your views here.
def logout_view(request):
    """Log the user out."""
    logout(request)
    return redirect("learning_logs:index")


def register(request):
    """Register a new User."""
    if request.method != "POST":
        # Display blank registration form.
        form = RegisterForm()
    else:
        # Process completed form.
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticate_user = authenticate(
                username=new_user.username, password=request.POST["password1"]
            )
            login(request, authenticate_user)
            return redirect("learning_logs:index")

    context = {"form": form}
    return render(request, "users/register.html", context)
