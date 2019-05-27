var service;
var map;
var request;
var placeicon;
var place;



function initMap() {

   // Create the map.
    var newyork = {lat: 40.7713024, lng: -73.9632393};
    map = new google.maps.Map(document.getElementById('map'), {
     center: newyork,
     zoom: 13
    });

    // converts user input of city or zipcode into latitude and longitude coordinates
    var geocoder = new google.maps.Geocoder();
    $("#submit").click(function() {
      geocodeAddress(geocoder, map);
    });
   

    // Create the places service.
    service = new google.maps.places.PlacesService(map);
    request = {
        location: newyork,
        radius: '200',
        query: 'Animal Adoption'
    };
    service.textSearch(request,callback);

}

function geocodeAddress(geocoder, resultsMap) {

  var address = $("#address").val();
  geocoder.geocode({'address': address}, function(results, status) {
    if (status === 'OK') {
      resultsMap.setCenter(results[0].geometry.location);
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
    request.location = results[0].geometry.location;
    service.textSearch(request,callback);
    $(".doggy-store").remove();

  });
}

function callback(results, status) {
    if (status == google.maps.places.PlacesServiceStatus.OK) {
        var infowindow = new google.maps.InfoWindow();
        var bounds = new google.maps.LatLngBounds();

        let newmarker = [];
        const redmarker = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png';
        const bluemarker = 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'

        for (var i = 0; i < results.length; i++) {

            // this creates markers on the map
            let place = results[i];
            newmarker[place.name] = new google.maps.Marker({
                position: place.geometry.location,
                map: map,
                title: place.name,
                address: place.formatted_address,
                image: place.photos,
                place_id: place.place_id,
                icon: redmarker,
                id: i
            });
      
            var ele = document.createElement("li");

            let store_title = [];
            store_title[i] = $("<div>", {text: place.name, class: "storename"});
            store_title[i].css({"fontWeight": 700, "width":175, "textAlign":"center"});
            ele.append(store_title[i][0]);

            let photoURL; 
            if (place.photos != null) {
                photoURL = place.photos[0].getUrl({'maxWidth':200,'maxHeight':200});
            } else {
                photoURL = "https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&dl=jamie-street-804226-unsplash.jpg";
            }

            let place_icon = [];
            place_icon[i] = $("<img>", {src: photoURL, class: "dogstoreimg", position: place.geometry.location});
            place_icon[i].css({"borderRadius": "25px", "width": 175, "height": 175});
            ele.append(place_icon[i][0]);

            address[i] = $("<div>", {text: place.formatted_address});
            address[i].css({"fontSize": "10px", "width": 175, "textAlign": "center"});
            ele.append(address[i][0]);

            let button = [];
            button[i] = $("<button>", {text: "Bookmark", id: "bookmark"});
            button[i].css({"backgroundColor": "salmon", "fontSize": "10px", "borderRadius": "25px", "textAlign": "center", "marginLeft": "45px"})
            ele.append(button[i][0]);

            ele.setAttribute("class","doggy-store");

            let check = [];
            check[i] = $("<img>", {src: "https://img.icons8.com/flat_round/26/000000/checkmark.png", id: place.name});
            check[i].css({"width":20, "marginLeft": "10px", "visibility": "hidden"});
            ele.append(check[i][0])
            
            $.get("/search.json",function (results){
              let names = results.name;
              if (names.includes(place.name)) {
                document.getElementById(place.name).style.visibility = "visible";
              } 
            })

            let checkStatus;
            button[i][0].addEventListener("click", function() {
                if (document.getElementById('myProfileBtn') === null) {
                  alert('You need to login or make an account to perform that action.');
                } else {
                  let checked = document.getElementById(place.name)
                  checkStatus = (checked.style.visibility ==='hidden');
                  if (checkStatus) {
                    checked.style.visibility = 'visible';
                  } else {  
                    checked.style.visibility = 'hidden';
                  }
                }
                let inputdata = {'message':'hello',
                                  'store_name': place.name,
                                  'store_address': place.formatted_address,
                                  'store_photo': photoURL,
                                  'check_status': checkStatus }
                $.post("/grab-data-from-frontend", inputdata, function(){})
              });

            $("#doggy-list").append(ele);

            newmarker[place.name].addListener('click',function() {
              if (this.image != null) {
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

             place_icon[i][0].addEventListener("mouseover", function() {
              this.style.cursor = "pointer";
              newmarker[place.name].setIcon(bluemarker);
              map.setCenter(place.geometry.location);
              map.zoom = 13;
            });
             place_icon[i][0].addEventListener("mouseout", function() {
              newmarker[place.name].setIcon(redmarker);
            });


            bounds.extend(place.geometry.location);
        }
        map.fitBounds(bounds);
    }
}




