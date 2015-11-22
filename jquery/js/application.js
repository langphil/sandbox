$(document).ready(function() {
	$('button').on('click', function() {
		var deal = $('<p>Dealz!</p>');
		$('.dealz').append(deal);
		$('button').remove();
	});
});