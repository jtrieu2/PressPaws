let service;
let map;
let request;
let placeicon;
let place;

function initMap() {

   // Create the map.
    let newyork = {lat: 40.7713024, lng: -73.9632393};
    map = new google.maps.Map(document.getElementById('map'), {
     center: newyork,
     zoom: 13
    });

    // converts user input of city or zipcode into latitude and longitude coordinates
    let geocoder = new google.maps.Geocoder();
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

  let address = $("#address").val();
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
        let infowindow = new google.maps.InfoWindow();
        let bounds = new google.maps.LatLngBounds();

        let newmarker = [];
        const redmarker = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png';
        const bluemarker = 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'

        for (let i = 0; i < results.length; i++) {

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

            let request = {
              placeId: place.place_id,
              fields: ['website','geometry','name','formatted_address','photos','place_id','opening_hours']
            }

            service = new google.maps.places.PlacesService(map);
            service.getDetails(request, function(place, status) {
              if (status === google.maps.places.PlacesServiceStatus.OK) {
                let ele = $("<li>");
                ele.css({"textAlign": "center", "width": 175});

                let store_title = [];
                store_title[i] = $("<div>", {text: place.name, class: "storename"});
                store_title[i].css({"fontWeight": 700, "width":175});
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
                address[i].css({"fontSize": "10px", "width": 175});
                ele.append(address[i][0]);

                let button = [];
                button[i] = $("<button>", {text: "Bookmark", id: "bookmark"});
                button[i].css({"backgroundColor": "salmon", "fontSize": "10px", "borderRadius": "25px"})
                ele.append(button[i][0]);


                let check = [];
                check[i] = $("<img>", {src: "https://img.icons8.com/flat_round/26/000000/checkmark.png", id: place.name});
                check[i].css({"width":20, "visibility": "hidden"});
                ele.append(check[i][0])

                let places = 'undefined'
                $.get("/search.json",function (results){
                  places = results.places;
                  if (places) {
                    if (places.includes(place.name)) {
                      document.getElementById(place.name).style.visibility = "visible";
                    } 
                  }
                })


                let web_url = [];
                let link = $("<div>");

                if (place.website) {
                  web_url[i] = $("<a>", {text: place.website });
                  web_url[i].attr("href", place.website);
                } else {
                  web_url[i] = $("<a>", {text: 'No website found.' });
                }
                  web_url[i].css({"fontSize": "10px", "width": 175});
                link.append(web_url[i][0]);
                ele.append(link);

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
                                      'business_hours': JSON.stringify(place.opening_hours.weekday_text),
                                      'business_website': place.website,
                                      'check_status': checkStatus }
                    $.post("/grab-data-from-frontend", inputdata, function(){})
                  });


                let business_hours;
                if (place.opening_hours) {
                      business_hours = $("<li>");
                      business_hours.css({"textAlign": "center"});
                  for (let i = 0; i < place.opening_hours.weekday_text.length; i++ ) {
                    let hours = $("<li>", {text: place.opening_hours.weekday_text[i]}); 
                    hours.css({"fontSize": "8px","textAlign": "center"});
                    business_hours.append(hours);
                  }
                } else {
                    business_hours = $("<li>", {text: 'No business hours listed'});
                    business_hours.css({"textAlign": "center","fontSize": "8px"});

                }
                ele.append(business_hours);

                ele.attr("class","doggy-store");
                $("#doggy-list").append(ele);

                newmarker[place.name].addListener('click',function() {
                  if (this.image != null) {
                       let content_str = ('<p id=infowindow>' + this.title + '</p>' +
                                          '<p id=infowindow>' + `<img src=${photoURL} align="middle">` + '</img>' + '</p>' +
                                          '<p id=infowindow>' + this.address + '</p>');

                  } else {
                       let content_str = ('<p id=infowindow>' + this.title + '</p>' +
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
                });

            
        }
        map.fitBounds(bounds);
    }
}




