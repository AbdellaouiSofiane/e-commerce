from django.db import models
from django.urls import reverse

from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
	translations = TranslatedFields(
		name = models.CharField(max_length=50),
		slug = models.SlugField(max_length=50)
	)
	
	class Meta:
		#ordering = ('name',)
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('shop:product_list', 
					   args=[self.slug])


class Product(TranslatableModel):
	translations = TranslatedFields(
		name = models.CharField(max_length=50),
		slug = models.SlugField(max_length=50),
		description = models.TextField(blank=True, null=True),
	)
	category = models.ForeignKey(Category, 
								 on_delete=models.CASCADE,
								 related_name='products')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	available = models.BooleanField(default=True)
	photo = models.ImageField(default='products/no_image.png',
							  upload_to='products/')
	price = models.DecimalField(max_digits=10, 
								decimal_places=2)

	#class META:
		#ordering = ('name',)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_detail', args=[self.id])
