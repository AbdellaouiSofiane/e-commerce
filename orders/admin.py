import csv
import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Order, Item



class ItemInline(admin.TabularInline):
	model = Item
	raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'email', 
				    'city', 'postal_code', 'created', 'paid', 'order_pdf']
	inlines = [ItemInline]
	actions = ['output_scv']

	@admin.action(description='output csv')
	def output_scv(self, request, queryset):
		opts = self.model._meta
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachement; '\
										  f'filename={opts.verbose_name}.csv'
		writer = csv.writer(response)
		fields = [field for field in opts.get_fields() if not \
					field.many_to_many and not field.one_to_many]
		writer.writerow([field.verbose_name for field in fields])
		# Write data rows
		for obj in queryset:
			data_row = []
			for field in fields:
				value = getattr(obj, field.name)
				if isinstance(value, datetime.datetime):
					value = value.strftime('%d/%m/%Y')
				data_row.append(value)
			writer.writerow(data_row)
		return response

	def order_pdf(self, obj):
		url = reverse('orders:order_pdf', args=[obj.id])
		return mark_safe(f'<a href="{url}">PDF</a>')

	order_pdf.short_description = 'Invoice'


