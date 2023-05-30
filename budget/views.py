from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import *

class HomeView(TemplateView):
    template_name = 'budget/home.html'

class RegisterView(SuccessMessageMixin, CreateView):
	form_class = UserCreationForm
	template_name = "registration/register.html"
	success_url = "/accounts/login"
	success_message = "Registration accepted. You can now log in. "

class RecurringPaymentListView(LoginRequiredMixin, ListView):
	model = RecurringPayment
        
	def get_queryset(self):
		return RecurringPayment.objects.filter(owner__username=self.request.user)
	
class RecurringPaymentCreateView(LoginRequiredMixin, CreateView):
	model = RecurringPayment
	fields = ['name', 'amount', 'url', 'category']
	success_url = "/payments"

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)