$(document).on('submit', '.signup-form', function(){
$.ajax({ 
    type: $(this).attr('method'), 
    url: this.action, 
    data: $(this).serialize(),
    context: this,
    success: function(data, status, xhr) {
        if (xhr.status == 278){
		window.location.replace(xhr.getResponseHeader("Location"));
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
    success: function(data, status, xhr) {
        if (xhr.status == 278){
		window.location.replace(xhr.getResponseHeader("Location"));
		} else {
	  $('#loginModal').html(data);
		}
    }
    });
    return false;
	
});