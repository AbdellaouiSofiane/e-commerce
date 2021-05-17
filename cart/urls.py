from django.urls import path 
from django.utils.translation import gettext_lazy as _
from . import views


app_name = 'cart'


urlpatterns = [
	path(_('add_to_cart/<int:product_id>/'), 
		 views.add_to_cart, 
		 name='add_to_cart'),
	path(_('remove_from_cart/<int:product_id>/'), 
		 views.remove_from_cart, 
		 name='remove_from_cart'),
	path(_('cart_detail/'), views.cart_detail, 
			name='cart_detail'),

]


