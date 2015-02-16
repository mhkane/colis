$(document).on('submit', '.auth-form', function(){
$.ajax({ 
    type: $(this).attr('method'), 
    url: this.action, 
    data: $(this).serialize(),
    context: this,
    success: function(data, status) {
        if (data.redirect){
		window.location.href = data.redirect;
		} else {
      $('#loginModal').html(data);
		}
    }
    });
    return false;
});