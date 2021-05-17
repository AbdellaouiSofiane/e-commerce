from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Product
from cart.forms import AddProductToCartForm
from .recommender import Recommender

def product_list(request, category_slug=None):
	categories = Category.objects.all()
	category = None
	products = Product.objects.filter(available=True)
	language = request.LANGUAGE_CODE
	if category_slug:
		category = get_object_or_404(Category, 
									translations__language_code=language,
									translations__slug=category_slug)
		products = products.filter(category=category)
	paginator = Paginator(products, 9)
	page_number = request.GET.get('page')
	products = paginator.get_page(page_number)
	context = {'products': products,
			   'categories': categories,
			   'category':category,}
	return render(request, 
				  'shop/product/list.html', 
				  context)


def product_detail(request, id):
	language = request.LANGUAGE_CODE
	product = get_object_or_404(Product, 
								id=id,
								translations__language_code=language,
								available=True)
	add_product_form = AddProductToCartForm()
	r = Recommender()
	recommended_products = r.suggest_products_for([product], 4)
	context = {
		'product': product,
		'add_product_form': add_product_form,
		'recommended_products': recommended_products
	}
	return render(request, 
				  'shop/product/detail.html', 
				  context)