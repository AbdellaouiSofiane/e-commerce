from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, \
								   MaxValueValidator

from shop.models import Product
from coupons.models import Coupon

class Order(models.Model):
	first_name = models.CharField(_('first_name'), max_length=50)
	last_name = models.CharField(_('last_name'), max_length=50)
	email = models.EmailField(_('email'))
	city = models.CharField(_('city'), max_length=50)
	address = models.CharField(_('address'), max_length=100)
	postal_code = models.CharField(_('postal_code'), max_length=10)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	braintree_id = models.CharField(max_length=150, blank=True)
	paid = models.BooleanField(default=False)
	coupon = models.ForeignKey(Coupon, 
							   on_delete=models.SET_NULL,
							   related_name='orders',
							   null=True,
							   blank=True)
	discount = models.IntegerField(default=0,
				validators=[MinValueValidator(0),
							MaxValueValidator(100)])

	def __str__(self):
		return f'order n°{self.id}'

	def get_total_discount(self):
		total_cost = sum(item.get_total_price() 
				for item in self.items.all())
		return total_cost * (self.discount / Decimal(100))

	def get_total_price(self):
		total_cost = sum(item.get_total_price() 
			for item in self.items.all())
		return total_cost - total_cost * \
			(self.discount / Decimal(100))


class Item(models.Model):
	order = models.ForeignKey(Order,
							  on_delete=models.CASCADE,
							  related_name='items')
	product = models.ForeignKey(Product, 
								on_delete=models.CASCADE)
	quantity = models.IntegerField()


	def __str__(self):
		return f'item: {self.quantity} * {self.product}'

	def get_total_price(self):
		return self.product.price * self.quantity




	