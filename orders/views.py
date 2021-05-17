import weasyprint
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings

from .forms import OrderCreateForm
from .models import Item, Order
from .tasks import order_created

from cart.cart import Cart
from shop.models import Product


def create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			if cart.coupon:
				order.coupon = cart.coupon
				order.discount = cart.coupon.discount
			order.save()
			for item in cart:
				Item.objects.create(order=order,
									product=item['product'],
									quantity=item['quantity'])
			cart.clear()
			request.session['order_id'] = order.id
			order_created.delay(order.id)
			return redirect(reverse('payment:process'))
	else :
		form = OrderCreateForm()
	return render(request, 'orders/create.html', 
						   {'form': form})

def created(request): 
	return render(request, 'orders/created.html')

def order_pdf(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
	html = render_to_string('orders/pdf.html', 
							{'order': order})
	weasyprint.HTML(string=html).write_pdf(response, 
		stylesheets=[weasyprint.CSS(
			settings.STATIC_ROOT + 'orders/css/pdf.css')])
	return response
