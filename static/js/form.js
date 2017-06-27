$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				topic : $('#topicInput').val(),
				query : $('#queryInput').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.callback).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});