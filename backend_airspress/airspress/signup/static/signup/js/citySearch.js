function distance_havesin(lat1, lon1, lat2, lon2) {
  var R = 6371; // Earth radius in kilometers
  var a = 
     0.5 - Math.cos((lat2 - lat1) * Math.PI / 180)/2 + 
     Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) * 
     (1 - Math.cos((lon2 - lon1) * Math.PI / 180))/2;

  return priceComp(Math.abs(R * 2 * Math.asin(Math.sqrt(a)) * 1000));
};
function distancePrice(){
	// Get the two locations geographical constants
	var latitude_dep = document.querySelector('input[name="location_lat1"]').value
	var longitude_dep = document.querySelector('input[name="location_lng1"]').value
	var latitude_arr = document.querySelector('input[name="location_lat2"]').value
	var longitude_arr = document.querySelector('input[name="location_lng2"]').value
	// Make latLng objects out of them
	var latLng1 = new google.maps.LatLng(latitude_dep, longitude_dep); 
	var latLng2 = new google.maps.LatLng(latitude_arr, longitude_arr);
	var distance_meters = google.maps.geometry.spherical.computeDistanceBetween(latLng1, latLng2);
	document.querySelector('input[name="distance"]').value = distance_meters;
	
	var price = 0;
	price = priceComp(distance_meters);
	if (price == 0){
		price = distance_havesin(latitude_dep, longitude_dep, latitude_arr, longitude_arr)
	}
	document.querySelector('input[name="unit_price"]').value = price;
	return price;
};
function priceComp(distance_meters){
	var price = 0;
	if (distance_meters) {
		if (distance_meters < 1000000) {
			price = 7;
		} else if (distance_meters < 2000000) {
			price = 10;
		} else if (distance_meters < 4000000) {
			price = 15;
		} else if (distance_meters < 6000000) {
			price = 17;
		};
	};	
	return price
};
function findComponent(result, type) {
  var component = _.find(result.address_components, function(component) {
    return _.include(component.types, type);
  });
  if (type == 'administrative_area_level_1'){
	return component && component.short_name + ', '+ component.long_name;
  };
  return component && component.long_name;
};
$(document).ready(function() {
		var options = {language: 'en-GB',types: ['(cities)']};
		var autocomplete1 = new google.maps.places.Autocomplete(self.$('#location1')[0], options);
		  
		google.maps.event.addListener(autocomplete1, 'place_changed', function() {
			var place = autocomplete1.getPlace();
			$('input[name="location_lat1"]').val(place.geometry.location.lat());
			$('input[name="location_lng1"]').val(place.geometry.location.lng());
			var country = findComponent(place, 'country');
			var state = findComponent(place, 'administrative_area_level_1');
			var city = findComponent(place, 'administrative_area_level_3') || findComponent(place, 'locality');
			$('input[name="location_country"]').val(country); 
			$('input[name="location_state"]').val(findComponent(place, 'administrative_area_level_1')); 
			if (country == 'United States' || country == 'Canada') {
					$('input[name="cityDep"]').val(city + ", " + state + ", " + country)
			} else { $('input[name="cityDep"]').val(city + ", " + country );}; 
		});
		var autocomplete2 = new google.maps.places.Autocomplete(self.$('#location2')[0], options);
		  
		google.maps.event.addListener(autocomplete2, 'place_changed', function() {
			var place2 = autocomplete2.getPlace();
			$('input[name="location_lat2"]').val(place2.geometry.location.lat());
			$('input[name="location_lng2"]').val(place2.geometry.location.lng());
			var country = findComponent(place2, 'country');
			var state = findComponent(place2, 'administrative_area_level_1');
			var city = findComponent(place2, 'administrative_area_level_3') || findComponent(place2, 'locality');
			$('input[name="location_country"]').val(country); 
			$('input[name="location_state"]').val(findComponent(place2, 'administrative_area_level_1')); 
			if (country == 'United States' || country == 'Canada') {
					$('input[name="cityArr"]').val(city + ", " + state + ", " + country)
			} else { $('input[name="cityArr"]').val(city + ", " + country );};
		});
		});