from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'orders'

urlpatterns = [
	path(_('create/'), views.create, name='create'),
	path(_('order/<int:order_id>/pdf/'), views.order_pdf, name='order_pdf'),
]