from django import forms

from .models import Payment 

class PaymentForm(forms.modelForm):
    class Meta:
        model = Payment
        exclude = []
