from typing import Any, Dict, Optional
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum

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
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		payments = RecurringPayment.objects.filter(owner=self.request.user)
		
		total_amount = payments.aggregate(total=Sum('amount'))['total']
		if total_amount is None:
			total_amount = 0.0

		context['total_amount'] = '{:.2f}'.format(total_amount)
		return context

class RecurringPaymentCreateView(LoginRequiredMixin, CreateView):
	model = RecurringPayment
	fields = ['category', 'name', 'amount', 'url']
	success_url = "/payments"

	def form_valid(self, form):
		form.instance.owner = self.request.user

		return super().form_valid(form)

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['category'].queryset = PaymentCategory.objects.filter(
            owner__username__in=[self.request.user.username, 'admin']
        )
		form.fields['category'].required = True
		return form


class RecurringPaymentUpdateView(UserPassesTestMixin, UpdateView):
	model = RecurringPayment
	fields = ['category', 'name', 'amount', 'url']
	success_url = "/payments"

	def test_func(self):
		object = self.get_object()
		return self.request.user == object.owner
	
	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['category'].queryset = PaymentCategory.objects.filter(
            owner__username__in=[self.request.user.username, 'admin']
        )
		return form
	

class RecurringPaymentDeleteView(UserPassesTestMixin, DeleteView):
	model = RecurringPayment
	success_url = "/payments"

	def test_func(self):
		object = self.get_object()
		return self.request.user == object.owner
	

class PaymentCategoryListView(LoginRequiredMixin, ListView):
	model = PaymentCategory

	def get_queryset(self):
		return PaymentCategory.objects.filter(owner__username=self.request.user)
	

class PaymentCategoryCreateView(LoginRequiredMixin, CreateView):
	model = PaymentCategory
	fields = ['name']
	success_url = "/categories"

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)


class PaymentCategoryUpdateView(UserPassesTestMixin, UpdateView):
	model = PaymentCategory
	fields = ['name']
	success_url = "/categories"

	def test_func(self):
		object = self.get_object()
		return self.request.user == object.owner
	

class PaymentCategoryDeleteView(UserPassesTestMixin, DeleteView):
	model = PaymentCategory
	success_url = "/categories"

	def test_func(self):
		object = self.get_object()
		return self.request.user == object.owner
	
