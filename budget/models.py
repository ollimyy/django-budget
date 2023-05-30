from django.db import models
from django.contrib.auth.models import User

class PaymentCategory(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class RecurringPayment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField(blank=True)
    category = models.ForeignKey(
        PaymentCategory, 
        on_delete=models.CASCADE,
        related_name='recurringPayments',
        blank=True)
    
    def __str__(self):
        return self.name
