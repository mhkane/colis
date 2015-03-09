$(document).on('submit', '.auth-form', function(){
$.ajax({ 
    type: $(this).attr('method'), 
    url: this.action, 
    data: $(this).serialize(),
    context: this,
    success: function(data, status) {
        if (data.redirect){
		window.location.replace("/trips");
		} else {
	  $('#signupModal').html(data);
		}
    }
    });
    return false;
});
$(document).on('submit', '.login-form', function(){
$.ajax({ 
    type: $(this).attr('method'), 
    url: this.action, 
    data: $(this).serialize(),
    context: this,
    success: function(data, status) {
        if (data.redirect){
		window.location.replace("/trips");
		} else {
	  $('#loginModal').html(data);
		}
    }
    });
    return false;
});