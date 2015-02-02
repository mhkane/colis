function findComponent(result, type) {
  var component = _.find(result.address_components, function(component) {
    return _.include(component.types, type);
  });
  return component && component.short_name;
}
$(document).ready(function() {
		var autocomplete1 = new google.maps.places.Autocomplete(self.$('#location1')[0], {types: ['geocode']});
		  
		google.maps.event.addListener(autocomplete1, 'place_changed', function() {
			var place = autocomplete1.getPlace();
			$('input[name="location_lat"]').val(place.geometry.location.lat());
			$('input[name="location_lng"]').val(place.geometry.location.lng());
			$('input[name="location_country"]').val(findComponent(place, 'country')); 
			$('input[name="location_state"]').val(findComponent(place, 'administrative_area_level_1')); 
			$('input[name="cityDep"]').val(findComponent(place, 'administrative_area_level_3') || findComponent(place, 'locality')); 
		});
		var autocomplete2 = new google.maps.places.Autocomplete(self.$('#location2')[0], {types: ['geocode']});
		  
		google.maps.event.addListener(autocomplete2, 'place_changed', function() {
			var place2 = autocomplete2.getPlace();
			$('input[name="location_lat"]').val(place2.geometry.location.lat());
			$('input[name="location_lng"]').val(place2.geometry.location.lng());
			$('input[name="location_country"]').val(findComponent(place2, 'country')); 
			$('input[name="location_state"]').val(findComponent(place2, 'administrative_area_level_1')); 
			$('input[name="cityArr"]').val(findComponent(place2, 'administrative_area_level_3') || findComponent(place2, 'locality')); 
		});
		});