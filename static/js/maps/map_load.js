/* define GLOBAL map_variable */
const labels = "C";
let label_index = 0;
let map;
let markers = [];
let marker

function re_center(map,selectedCounty,propertyLocation){
  var newCenter = myCenter;
  
  console.log('selectedCounty is '+selectedCounty);
  
  if("Clare"==selectedCounty){
    newCenter = clareCenter;
  }
    else if("Cork"==selectedCounty){
    newCenter=corkCenter;
  }
    else if("Cavan"==selectedCounty){
    newCenter=cavanCenter;
  }
    else if("Carlow"==selectedCounty){
    newCenter=carlowCenter;
  }
    else if("Donegal"==selectedCounty){
    newCenter=donegalCenter;
  }
    else if("Dublin"==selectedCounty){
    newCenter=dublinCenter;
  }
    else if("Galway"==selectedCounty){
    newCenter=galwayCenter;
  }
    else if("Kildare"==selectedCounty){
    newCenter=kildareCenter;
  }
    else if("Kilkenny"==selectedCounty){
    newCenter=kilkennyCenter;
  }
    else if("Kerry"==selectedCounty){
    newCenter=kerryCenter;
  }
    else if("Longford"==selectedCounty){
    newCenter=longfordCenter;
  }
    else if("Louth"==selectedCounty){
    newCenter=louthCenter;
  }
    else if("Limerick"==selectedCounty){
    newCenter=limerickCenter;
  }
    else if("Leitrim"==selectedCounty){
    newCenter=leitrimCenter;
  }
    else if("Laois"==selectedCounty){
    newCenter=laoisCenter;
  }
    else if("Meath"==selectedCounty){
    newCenter=meathCenter;
  }
    else if("Monaghan"==selectedCounty){
    newCenter=monaghanCenter;
  }
    else if("Mayo"==selectedCounty){
    newCenter=mayoCenter;
  }
    else if("Offaly"==selectedCounty){
    newCenter=offalyCenter;
  }
    else if("Roscommon"==selectedCounty){
    newCenter=roscommonCenter;
  }
    else if("Sligo"==selectedCounty){
    newCenter=sligoCenter;
  }
    else if("Tipperary"==selectedCounty){
    newCenter=tipperaryCenter;
  }
    else if("Waterford"==selectedCounty){
    newCenter=waterfordCenter;
  }
    else if("Westmeath"==selectedCounty){
    newCenter=westmeathCenter;
  }
    else if("Wicklow"==selectedCounty){
    newCenter=wicklowCenter;
  }
    else if("Wexford"==selectedCounty){
    newCenter=wexfordCenter;
  }
    else if("Fermanagh"==selectedCounty){
    newCenter=fermanaghCenter;
  }
    else if("Tyrone"==selectedCounty){
    newCenter=tyroneCenter;
  }
    else if("Derry"==selectedCounty){
    newCenter=derryCenter;
  }
    else if("Down"==selectedCounty){
    newCenter=downCenter;
  }
    else if("Antrim"==selectedCounty){
    newCenter=antrimCenter;
  }
    else if("Armagh"==selectedCounty){
    newCenter=armaghCenter;
  }
  
  console.log('recentering');
  
  // recentre the mao based on county
  map.setCenter(newCenter);
	map.setZoom(9);
	console.log('centered');
	
	//  add the marker to the map based on property location
  add_marker(propertyLocation,map);
  //populate_lat_lng(propertyLocation);
  
}

// Set the map sented depending on the Lat & Lng received
function populate_lat_lng(newCenter){
  console.log('loading lat and lng');
  console.log(newCenter);
  console.log(newCenter['lat']);
  console.log(newCenter['lng']);
  $('#id_latitude').val(newCenter['lat']).prop("readonly", true);
  $('#id_longitude').val(newCenter['lng']).prop("readonly", true);  ;
}


// ADD MARKER to the map at the property location and push to the MARKER array
function add_marker(propertyLocation,map){

      //  clear any pre-existing markers
      delete_markers();
      
      console.log('markers deleted');

      marker = new google.maps.Marker({
        position: propertyLocation,
        //position = new google.maps.LatLng(latitude,longitude),
        label: labels[label_index++ % labels.length],
        map: map, 
        draggable: true,
      });
      
      //console.log('markers object created');
      
      markers.push(marker);
      var pos = marker.getPosition();
      //console.log(pos);
      
      marker.addListener('drag',function(event) {
        //populate_lat_lng(event.latLng);
      });
      
      marker.addListener('dragend',function(event) {
        //populate_lat_lng(event.latLng);
      });
}

// adds all markers in the marker array to the map
function set_map_on_all(map){
  
  //console.log('in set_map_on_all function');
  //console.log('markers length');
  //console.log(markers.length);
  
  for (let i = 0; i < markers.length; i++){
    console.log('setting marker on map');
    //  set the marker on the map
    markers[i].setMap(map);
    
    console.log('the marker url is '+markers[i].url);
    
    // add a click event listener to the marker so that it becomes a link
    google.maps.event.addListener(markers[i], 'click', function() {
      console.log('marker clicked');
      
      window.location.href = markers[i].url;
    });
    
    
  }
}

// show any markers currently in the marker array
function show_markers(){
  set_map_on_all(map);
}
  

// remove the markers in the marker array from the map, but keep them in the array
function hide_markers(){
  set_map_on_all(null);
}


// Delete all markers from the marker array, which will remove them from teh map
function delete_markers(){
  hide_markers();
  markers = [];
}

/////////////////////////////////////////////////////////////////////////
//
//  MAP initialiser functions
//  
/////////////////////////////////////////////////////////////////////////


function init_property_profile_map(){
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 7,
        center: myCenter,
    });
    
    add_marker(dublinCenter,map)
    populate_lat_lng(dublinCenter);
    
    
    //  recenter the marker based on county
    //  and retrieve the latitude and longitude for the property
    var selectedCounty = $('#id_county').text();
    var latitude = parseFloat($('#id_latitude').text());
    var longitude = parseFloat($('#id_longitude').text());

    console.log('selectedCounty is '+selectedCounty+' lat='+latitude+' lng='+longitude);
    console.log('latitude is numeric ='+$.isNumeric(latitude));
    console.log('longitude is numeric ='+$.isNumeric(longitude));
    
    var propertyLocation = new google.maps.LatLng(parseFloat(latitude), parseFloat(longitude)); 
    
    //propertyMapMarker = {lat:latitude, lng:longitude};
    
    re_center(map,selectedCounty,propertyLocation);
  
}


function add_property_add_form_controls(){
  $('#id_property_type').addClass("form-control")
  $('#id_listing_type').addClass("form-control")
  $('#id_street_address').addClass("form-control")
  $('#id_county').addClass("form-control")
  $('#id_latitude').addClass("form-control")
  $('#id_longitude').addClass("form-control")
  $('#id_bedrooms').addClass("form-control")
  $('#id_ber_rating').addClass("form-control")
  $('#id_description').addClass("form-control")
  $('#id_price').addClass("form-control")
  $('#id_agent_email').addClass("form-control")
}


function init_property_add_map(){

    /**
     * Load the initial map with marker set to first County in menu ---Antrim
     */ 
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 7,
        center: myCenter,
    });
    add_marker(dublinCenter,map);
    populate_lat_lng(dublinCenter);
    
    
    /**
     *  Event Listener calls addMarker when the map is clicked
     *  Also retrieves the Latitured and Longitude of the marker
     */ 
    google.maps.event.addListener(map,"click",(event) => {
        add_marker(event.latLng, map);
        populate_lat_lng(event.latLng);
    });
    
        //  Select the county to focus on
    $("#id_county").change(function() {
        console.log('item changed');
        var selectedCounty = $('#id_county option:selected').text();
        console.log(selectedCounty);
        re_center(map,selectedCounty);
    });
}

//  populate the map for teh listing page
function init_property_list_map(){
  
  //  clear the map of any markers
  delete_markers();
  
  //  create the map and center it
  map = new google.maps.Map(document.getElementById("map"), {
      zoom: 7,
      center: myCenter,
  });

  //  create array to create and hold the markers for each of the proprties on the page
  //var propertyArr = [];
  $('.card_lat_long').each(function () { // <-- Missed { here
      strPos = $(this).text();
      
      console.log($(this).text());
      strPosArr = strPos.split(",")
      var propertyLocation = new google.maps.LatLng(parseFloat(strPosArr[0]), parseFloat(strPosArr[1])); 
      //markers.push(propertyLocation);
      
      marker = new google.maps.Marker({
        position: propertyLocation,
        label: labels[label_index++ % labels.length],
        map: map, 
        url: strPosArr[2],    //  Retrieve the URL from the string passed in
        draggable: true,
      });
      
      markers.push(marker);
      var pos = marker.getPosition();
      console.log(pos);
      
  });
  
  //  populate the map with the markers in the markers array
  set_map_on_all(map,);

}