from django.shortcuts import render,  get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from shop.models import Product

from .forms import AddProductToCartForm
from .cart import Cart
from coupons.forms import CouponApplyForm
from shop.recommender import Recommender

@require_POST
def add_to_cart(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, 
								id=product_id,
								available=True)
	add_product_form = AddProductToCartForm(request.POST)
	if add_product_form.is_valid():
		cd = add_product_form.cleaned_data
		quantity = cd['quantity']
		cart.add(product, quantity)
		
	if request.is_ajax():
		
		return JsonResponse({
			'items_count': str(len(cart)),
			'item_total_price': str(quantity* product.price),
			'cart_subtotal_price' : str(cart.get_total_price()),
			'cart_discount': str(cart.get_discount()),
			'cart_total_price': str(cart.get_total_price_after_discount()),
		})
	else:
		return redirect(reverse('cart:cart_detail'))

@require_POST
def remove_from_cart(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, 
								id=product_id,
								available=True)
	cart.remove(product)
	return redirect(reverse('cart:cart_detail'))


def cart_detail(request):
	coupon_apply_form = CouponApplyForm()
	cart = Cart(request)
	recommended_products = None
	if len(cart) != 0 :
		r = Recommender()
		cart_products = [item['product'] for item in cart]
		recommended_products = r.suggest_products_for(
			cart_products,
			max_results=4)
	return render(request, 'cart/detail.html', 
					{'coupon_apply_form': coupon_apply_form,
					 'recommended_products': recommended_products})