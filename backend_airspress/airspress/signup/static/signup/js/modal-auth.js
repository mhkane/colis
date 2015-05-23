
$(document).on('submit', '.signup-form', function(){
document.getElementById("checkbox1").checkValidity();
var state = true;
document.getElementById("checkbox1").value = state;
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
	  $($(this).attr('modal')).html(data);
		}
    }
    });
    return false;
	
});