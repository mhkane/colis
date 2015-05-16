function ajaxSend(form){
	$.ajax({ 
    type: $(form).attr('method'), 
    url: form.action, 
    data: $(form).serialize(),
    context: form,
    success: function(data, status, xhr) {
        if (xhr.status == 278){
		window.location.replace(xhr.getResponseHeader("Location"));
		} else {
	  $('#signupModal').html(data);
		}
    }
    });
	
}
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
    event.preventDefault();
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