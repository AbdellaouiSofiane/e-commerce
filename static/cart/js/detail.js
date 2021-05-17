$(document).ready(function(){
	$('.update_quantity_form').on('change', function(e){
		var productId = $(this).data('id')
		$.post($(this).data('url'), {
			'quantity': e.target.value,
		}, function(response) {
			$('#cart_total_price').html('$ ' + response.cart_total_price);
			$('#item-price-'+ productId).html('$ ' + response.item_total_price);
			$('#cart-items').html(response.items_count);
		});
	});	

});