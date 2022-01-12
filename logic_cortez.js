// Create a map object.
var myMap = L.map("map", {
    center: [37.09, -95.71],
    zoom: 5
  });
  
  // Add a tile layer.
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);
  
 // Link to weather data
 var link = "https://api.weather.gov/points/37.09,-95.71";

var options = {
  radius:8,
  fillColor:'#ff7800',
  color:'#000',
  weight:1,
  opacity:1,
  fillOpacity:.08
}


// Getting our GeoJSON data
d3.json(link).then(function(data) {console.log(data);
  // Creating a GeoJSON layer with the retrieved data
  L.geoJson(data,{
      pointToLayer:function(feature,latlng){
        return L.circleMarker(latlng,options);
      }


  }).addTo(myMap);
});



// other option

function onEach(feature, layer){
  if (feature.properties && feature.properties.popupContent) {
    layer.bindPopup(feature.properties.popupContent)
  }
}

d3.json(link).then(function(data){
  L.geoJSON(data,{
    onEachFeature: onEach
  }).addTo(myMap);
})


