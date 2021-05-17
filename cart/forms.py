from django import forms 
from django.utils.translation import gettext_lazy as _


class AddProductToCartForm(forms.Form):
	QUANTITY_CHOICES = [(i, str(i)) for i in range(1,11)]
	quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES,
									  coerce=int,
									  label=_('quantity'))