from decimal import Decimal
from shop.models import Product
from cart.forms import AddProductToCartForm
from coupons.models import Coupon



class Cart(object):
	def  __init__(self, request):
		self.session = request.session
		if not self.session.get('cart'):
			cart = self.session['cart'] = {}
		else: 
			cart = self.session['cart']
		self.cart  = cart
		self.coupon_id = self.session.get('coupon_id')

	def add(self, product, quantity):
		product_id = str(product.id)
		self.cart[product_id] = {
			'quantity': quantity
		}
		self.save()

	def remove(self, product):
		product_id = str(product.id)
		del self.cart[product_id]
		self.save()

	def __iter__(self):
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)

		cart = self.cart.copy()
		for product in products:
			cart[str(product.id)]['product'] = product

		for item in cart.values():
			item['total_price'] = item['product'].price * item['quantity']
			item['quantity_form'] = AddProductToCartForm(
										initial={'quantity': item['quantity']})
			yield item

	def __len__(self):
		return sum([item['quantity'] for item in self.cart.values()])

	def get_total_price(self):
		return sum([Product.objects.get(id=product_id).price * item['quantity']
			for product_id ,item in self.cart.items()])

	def save(self):
		self.session.modified = True


	def clear(self):
		del self.session['cart']
		self.save()

	@property
	def coupon(self):
		if self.coupon_id:
			try:
				return Coupon.objects.get(id=self.coupon_id)
			except Coupon.DoesNotExist:
				pass
		return None

	def get_discount(self):
		if self.coupon:
			return round((Decimal(self.coupon.discount) / Decimal(100)) \
						* self.get_total_price(), 2)
		return Decimal(0)

	def get_total_price_after_discount(self):
		return self.get_total_price() - self.get_discount()

	
