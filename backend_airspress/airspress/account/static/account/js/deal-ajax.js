$(document).on('submit', '#popover-form', function(){
$.ajax({ 
    type: $(this).attr('method'), 
    url: this.action, 
    data: $(this).serialize(),
    context: this,
    success: function(data, status, xhr) {
        if (xhr.status == 278){
			window.location.replace(xhr.getResponseHeader("Location"));
		} else {
			$('#notification').html(data);
			window.setTimeout(function() {
					$("#notification").fadeTo(1500, 0).slideUp(500, function(){
					$(this).hide(); 
				});
			}, 5000);
		}
    }
    });
    return false;
	
});