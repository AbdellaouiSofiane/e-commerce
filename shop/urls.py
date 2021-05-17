from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'shop'

urlpatterns = [
	path('', views.product_list, name='product_list'),
	path('<slug:category_slug>/', views.product_list, name='product_list'),
	path(_('product/<int:id>/'), 
		 views.product_detail, 
		 name='product_detail'),
]