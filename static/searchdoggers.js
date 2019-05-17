var service;
var map;
var request;
var placeicon;


function initMap() {

   // Create the map.
    var newyork = {lat: 40.7713024, lng: -73.9632393};
    map = new google.maps.Map(document.getElementById('map'), {
     center: newyork,
     zoom: 13
    });

   var geocoder = new google.maps.Geocoder();

    document.getElementById('submit').addEventListener('click', function() {
    geocodeAddress(geocoder, map);
    });

    // Create the places service.
    //var new_location = geocodeAddress(geocoder,map);
    service = new google.maps.places.PlacesService(map);
    request = {
        location: newyork,
        radius: '200',
        query: 'Animal Adoption'
    };
    //alert(request.location)
    service.textSearch(request,callback);

}

function geocodeAddress(geocoder, resultsMap) {
  var address = document.getElementById('address').value;
  geocoder.geocode({'address': address}, function(results, status) {
    if (status === 'OK') {
      resultsMap.setCenter(results[0].geometry.location);
      // var marker = new google.maps.Marker({
      //   map: resultsMap,
      //   position: results[0].geometry.location
      // });
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }


    // update nearby search 
    //var doglist = document.querySelector(".PetShopsContiner");
    var ele = document.getElementById('dog-store');
    ele.innerHTML = 'bye';

    request.location = results[0].geometry.location;
    service.textSearch(request,callback);
    var elements = document.getElementsByClassName("dog-store");
    alert(elements.length);
    $(".dog-store").remove();

  });
}



function callback(results, status) {
    if (status == google.maps.places.PlacesServiceStatus.OK) {
        var infowindow = new google.maps.InfoWindow();
        var bounds = new google.maps.LatLngBounds();

        for (var i = 0; i < results.length; i++) {

            // this creates markers on the map
            var place = results[i];
            var newmarker = new google.maps.Marker({
                position: place.geometry.location,
                map: map,
                title: place.name,
                address: place.formatted_address,
                image: place.photos,
                place_id: place.place_id,
                id: i
            });

            // this creates clickable icons on the left
            var ele = document.createElement("li");
            var div = document.createElement("div");
            var divtext = document.createTextNode(place.name);
            var placeicon = document.createElement("img");

            if (place.photos != null) {
                var photoURL = place.photos[0].getUrl({'maxWidth':200,'maxHeight':200});
                placeicon.setAttribute("src", photoURL);
            } else {
                placeicon.setAttribute("src","https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=jamie-street-804226-unsplash.jpg");
            }
            placeicon.setAttribute("width",175);
            placeicon.setAttribute("height",175);
            placeicon.setAttribute("id","dog-store");
            placeicon.style.borderRadius = '25px';
            ele.appendChild(divtext);
            ele.appendChild(div);
            ele.appendChild(placeicon);
            ele.setAttribute("display","block");
            ele.setAttribute("width",100);
            item = document.getElementById('doggy-list');
            item.appendChild(ele);

            newmarker.addListener('click',function() {
              if (this.image != null) {
                   var photoURL = this.image[0].getUrl({'maxWidth':200,'maxHeight':200});
                   var content_str = ('<p id=infowindow>' + this.title + '</p>' +
                                      '<p id=infowindow>' + `<img src=${photoURL} align="middle">` + '</img>' + '</p>' +
                                      '<p id=infowindow>' + this.address + '</p>');


              } else {
                   var content_str = ('<p id=infowindow>' + this.title + '</p>' +
                                      '<p id=infowindow>' + this.address + '</p>');
              }
              infowindow.setContent(content_str);
              infowindow.open(map,this);
            });

            bounds.extend(place.geometry.location);
        }
            
        map.fitBounds(bounds);
    }
}




