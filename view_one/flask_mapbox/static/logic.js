// Creating map object
var map = L.map("map", {
  center: [26.33, 17.22],
  zoom: 1.5
});

// Adding tile layer
L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?'+
        'access_token=pk.eyJ1IjoiamlpbnJvIiwiYSI6ImNqZWxwaDI0YjRsaTMyd3FlOXRqcnFpa3EifQ.GP3cmOS9nkdW3pbk4jEwQQ').addTo(map);



var server_link = 'http://127.0.0.1:5000/region_intensities'

// Grabbing our GeoJSON data..
d3.json(server_link, function(error, response) {
  // Creating a GeoJSON layer with the retrieved data
  if (error) return console.warn(error);

  
  console.log(server_link)
  console.log(response)

  // L.geoJson(data).addTo(map);
});




  
