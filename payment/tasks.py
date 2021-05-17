from io import BytesIO

import weasyprint
from celery import shared_task

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from orders.models import Order


@shared_task
def payment_complete(order_id):
	order = Order.objects.get(id=order_id)
	subject = f'Invoice n°{order.id}'
	message = f'Please find attached your invoice'
	email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])
	out = BytesIO()
	html = render_to_string('orders/pdf.html', {'order': order})
	stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'orders/css/pdf.css')]
	weasyprint.HTML(string=html).write_pdf(out,
							stylesheets=stylesheets)
	email.attach(f'order_{order.id}.pdf',
				 out.getvalue(),
				 'application/pdf')
	email.send()