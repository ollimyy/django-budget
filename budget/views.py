from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm

class HomeView(TemplateView):
    template_name = 'budget/home.html'

class RegisterView(SuccessMessageMixin, CreateView):
	form_class = UserCreationForm
	template_name = "registration/register.html"
	success_url = "/accounts/login"
	success_message = "Registration accepted. You can now log in. "
