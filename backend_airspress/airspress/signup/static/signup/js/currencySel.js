
 function displayModal(event) {
    event.preventDefault();
	try{
		var target = $(this).attr("href");
		$.ajax({
			url: target,
			type: 'GET',
			success: function(response, status, xhr) {
			if (xhr.status == 278){
				window.location.replace(xhr.getResponseHeader("Location"));
				} else {
			  $('#modal').html(response).modal("show");
			}}
		 });
    } catch(err){
		window.location.replace("/signup")
	
	}
};
function saveForm(e) {
  e.preventDefault();

  $.ajax({
    url: $('#modal-form').attr('action'),
    type: $('#modal-form').attr('method'),
    data: $('#modal-form').serialize(),
    success: function(response, status, xhr) {
	if (xhr.status == 278){
		window.location.replace(xhr.getResponseHeader("Location"));
		} else {
      $('#modal').html(response);
    }}
 });
 
 
};
 function updateCurrency() {
    //get the selected value
    var selectedValue = this.value;

    //make the ajax call
    $.ajax({
        url: 'function.php',
        type: 'POST',
        data: {option : selectedValue},
        success: function(json) {
              $('.unit-price').append( json.server_response);
        }
        });
    };