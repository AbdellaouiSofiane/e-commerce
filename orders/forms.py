from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = ('paid', 'braintree_id', 'coupon', 'discount')