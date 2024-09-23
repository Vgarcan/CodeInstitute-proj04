from django.shortcuts import render
from allauth.account.views import LoginView, SignupView
# Create your views here.


def home(request):
    """
    This function renders the home page of the application.

    Parameters:
    request (HttpRequest): The request object that contains information about the current web request.

    Returns:
    HttpResponse: The rendered home page template.
    """
    return render(request, 'users/home.html')


class CustomLoginView(LoginView):  # CBV
    """
    Custom Login view
    """
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        # Add extra data to the context for the template
        context = super().get_context_data(**kwargs)
        context["extra_message"] = "Loging View from Users APP"
        return context


class CustomSignupView(SignupView):  # CBV
    """
    Custom Signup view
    """
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        # Add extra data to the context for the template
        context = super().get_context_data(**kwargs)
        context["extra_message"] = "Loging View from Users APP"
        return context
